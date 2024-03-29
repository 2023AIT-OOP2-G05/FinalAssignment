from abc import ABC, abstractmethod

class processorBase(ABC):

    @abstractmethod
    def process(self, filepath, savePath):
        pass