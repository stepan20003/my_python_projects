from abc import abstractmethod, ABC
from typing import Any, Protocol


class JSONexpand:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_string = "{"
        for i, (rank, value) in enumerate(data):
            json_string += f'item_{rank}: "{value}"'
            if i < len(data) - 1:
                json_string += ", "
        json_string += "}"
        print(json_string)


class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            print("")
            return
        csv = ""
        nee = len(data)
        for value in data:
            if data[nee - 1] == value:
                csv += f"{value[1]}"
                break
            csv += f"{value[1]},"
        print("CSV Output:")
        print(csv)


class DataProcessor(ABC):
    def __init__(self):
        self.storage = []
        self.count = 0
        self.data_processor = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> Any:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise ValueError("No data")

        value = self.storage.pop(0)
        rank = self.count
        self.count += 1
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            if all(isinstance(item, (int, float))
                    and not isinstance(item, bool) for item in data):
                return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, (int, float)):
                self.storage.append(str(data))
                self.data_processor += 1
            if isinstance(data, list):
                for i in data:
                    self.storage.append(str(i))
                    self.data_processor += 1
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            if all(isinstance(item, (str)) for item in data):
                return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, (str)):
                self.storage.append(data)
                self.data_processor += 1
            if isinstance(data, list):
                for i in data:
                    self.storage.append(i)
                    self.data_processor += 1
        else:
            raise ValueError("Invalid data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_dict(data: Any) -> bool:
            return isinstance(data, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
                )

        if valid_dict(data):
            return True
        if isinstance(data, list):
            return all(valid_dict(d) for d in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> Any:
        def format(d: dict[str, str] | list[dict[str, str]]) -> Any:
            return ": ".join(f"{v}" for v in d.values())

        if self.validate(data):
            if isinstance(data, (dict)):
                self.storage.append(format(data))
                self.data_processor += 1
            if isinstance(data, list):
                for i in data:
                    self.storage.append(format(i))
                    self.data_processor += 1
        else:
            raise ValueError("Invalid data")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self):
        self.processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for i in stream:
            for proc in self.processor:
                if proc.validate(i):
                    try:
                        proc.ingest(i)
                        break
                    except Exception:
                        break

        if not stream:
            print("No processor found, no data\n")

    def print_pocessors_stats(self) -> None:
        for i in self.processor:
            if isinstance(i, NumericProcessor):
                print(f"Numeric Processor: total {i.data_processor} items"
                      f" processed, remaining {len(i.storage)} on processor")
            if isinstance(i, TextProcessor):
                print(f"Text Processor: total {i.data_processor} items"
                      f" processed, remaining {len(i.storage)} on processor")
            if isinstance(i, LogProcessor):
                print(f"Log Processor: total {i.data_processor} items"
                      f" processed, remaining {len(i.storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        leng = nb
        processors = self.processor.copy()
        for i in processors:
            collected = []
            nb = leng
            while nb > 0 and len(i.storage) > 0:
                collected.append(i.output())
                nb -= 1
            plugin.process_output(collected)


if __name__ == "__main__":

    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    proc = DataStream()
    lst1 = [text, log]
    proc.register_processor(num)
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    print("== DataStream statistics ==")
    proc.process_stream([])
    print("Registering Processors")
    lst2 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
              "log_level": "INFO",
              "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {lst2}")
    print("== DataStream statistics ==")
    for i in lst1:
        proc.register_processor(i)

    proc.process_stream(lst2)
    proc.print_pocessors_stats()
    csv = CSVExporter()
    proc.output_pipeline(3, csv)
    print("\n== DataStream statistics ==")
    proc.print_pocessors_stats()
    lst3 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificateexpires in 10 days'}],
            [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {lst3}")
    print("\n== DataStream statistics ==")
    proc.process_stream(lst3)
    proc.print_pocessors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json = JSONexpand()
    proc.output_pipeline(5, json)
    print("\n== DataStream statistics ==")
    proc.print_pocessors_stats()
