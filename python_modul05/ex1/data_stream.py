from abc import abstractmethod, ABC
from typing import Any


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


class DataStream:
    def __init__(self):
        self.processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for i in stream:
            handled = False
            for proc in self.processor:
                if proc.validate(i):
                    try:
                        proc.ingest(i)
                        handled = True
                        break
                    except Exception:
                        handled = True
                        break
            if not handled:
                print("no data")
            





if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    lst1 = [1, 2, 3, 4, 5]
    print(f" Processing data: {lst1}")
    i = 3
    print(f" Extracting {i} values...")
    if num.validate(lst1):
        num.ingest(lst1)
        for i in range(i):
            r, v = num.output()
            print(f" Numeric value {r}: {v}")

    print("\nTesting Text Processor...")
    print(f" Trying to validate input '42': {text.validate(42)}")
    lst2 = ['Hello', 'Nexus', 'World']
    if text.validate(lst2):
        print(f" Processing data: {lst2}")
        text.ingest(lst2)
        print(" Extracting 1 value...")
        r, v = text.output()
        print(f" Text value {r}: {v}\n")

    print("Testing Log Processor...")
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    lst3 = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    if log.validate(lst3):
        log.ingest(lst3)
        print(f" Processing data: {lst3}")
        print(" Extracting 2 values...")
        for i in range(2):
            r, v = log.output()
            print(f" Log entry {r}: {v}")
