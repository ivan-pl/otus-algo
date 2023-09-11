from abc import ABC, abstractmethod
import numpy as np


class BaseArray(ABC):
    def __init__(self, dtype=str):
        self._values = np.array([], dtype)
        self._dtype = dtype
        self.size = 0

    @abstractmethod
    def add(self, item, index=None):
        pass

    @abstractmethod
    def remove(self, index):
        pass

    def __repr__(self):
        return str(self._values[:self.size])

    def __getitem__(self, i):
        return self._values[i]

    def __len__(self):
        return self.size
