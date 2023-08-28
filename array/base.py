from abc import ABC, abstractmethod
import numpy as np


class BaseArray(ABC):
    def __init__(self, d_type=str):
        self.array = np.array([], d_type)
        self.size = 0

    @abstractmethod
    def add(self, item, index):
        pass

    @abstractmethod
    def remove(self, index):
        pass
