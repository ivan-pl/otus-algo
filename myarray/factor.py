import numpy as np
from .base import BaseArray


class FactorArray(BaseArray):
    def __init__(self, dtype=str, factor=0.3):
        super().__init__(dtype)
        self._factor = factor

    def add(self, item, index=None):
        if index is None:
            index = self.size
        if index > self.size:
            raise IndexError()
        new_size = self.size + 1
        if new_size > self._values.size:
            new_values = np.empty(self._calculate_new_size(), dtype=self._dtype)
            for i in range(index):
                new_values[i] = self._values[i]
            new_values[index] = item
            for i in range(index + 1, self.size + 1):
                new_values[i] = self._values[i - 1]
            self._values = new_values
        else:
            for i in range(new_size - 1, index, -1):
                self._values[i] = self._values[i - 1]
            self._values[index] = item
        self.size = new_size
        return self

    def remove(self, index):
        if index >= self.size:
            return self
        self.size -= 1
        if (self._values.size - self.size) / self._values.size > self._factor:
            new_values = np.empty(self._calculate_new_size(remove_factor=True), dtype=self._dtype)
            for i in range(index):
                new_values[i] = self._values[i]
            for i in range(index + 1, self.size + 1):
                new_values[i - 1] = self._values[i]
            self._values = new_values
        else:
            for i in range(index, self.size):
                self._values[i] = self._values[i + 1]
        return self

    def _calculate_new_size(self, remove_factor=False):
        if remove_factor:
            return self.size + round(self.size * self._factor * 0.5 / 100) + 1
        return self.size + round(self.size * self._factor / 100) + 1


if __name__ == "__main__":
    arr = FactorArray(int, 2)
    arr.add(0).add(1).add(2).remove(1).add(5).add(6, 0).remove(3)
    print(arr)
