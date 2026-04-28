from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.storage = []
        self.count = 0
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

    def ingest(self, data: int | float | list[int | float]) -> Any:
        if self.validate(data):
            if isinstance(data, (int, float)):
                self.storage.append(str(data))
            if isinstance(data, list):
                for i in data:
                    self.storage.append(str(i))
        else:
            raise ValueError("Invalid data")
        return self.storage
    

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            if all(isinstance(item, (str)) for item in data):
                return True
        return False

    def ingest(self, data: str | list[str]) -> Any:
        if self.validate(data):
            if isinstance(data, (str)):
                self.storage.append(data)
            if isinstance(data, list):
                for i in data:
                    self.storage.append(i)
        else:
            raise ValueError("Invalid data")
        return self.storage


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_dict(data) -> bool:
            return isinstance(data, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.item
                )

        if valid_dict(data):
            return True
        if isinstance(data, list):
            return all(valid_dict(d) for d in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> Any:
        def format(d):
            return "".join(f"{k}:{v}" for k, v in d.items())

        if self.validate(data):
            if isinstance(data, (dict)):
                self.storage.append(format(data))
            if isinstance(data, list):
                for i in data:
                    self.storage.append(format(i))
        else:
            raise ValueError("Invalid data")
