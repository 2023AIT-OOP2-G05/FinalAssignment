from abc import ABC, abstractmethod

class processorBase(ABC):

    @abstractmethod
    def process(self, image_path, filepath, factor):
        pass