from abc import ABC, abstractmethod


class JsonSerializable(ABC):
    @abstractmethod
    def to_json(self):
        pass
