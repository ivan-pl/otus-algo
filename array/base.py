from abc import ABC, abstractmethod
import numpy as np


class BaseArray(ABC):
    def __init__(self, dtype=str):
        self._values = np.array([], dtype)
        self._dtype = dtype
        self.size = 0

    @abstractmethod
    def add(self, item, index):
        pass

    @abstractmethod
    def remove(self, index):
        pass
