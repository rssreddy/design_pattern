from abc import ABC, abstractmethod
class OS(ABC):

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError
