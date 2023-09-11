import numpy as np
from base import BaseArray


class VectorArray(BaseArray):
    def __init__(self, dtype, vector=10):
        super().__init__(dtype)
        self._vector = vector

    def add(self, item, index=None):
        if index is None:
            index = self.size
        if index > self.size:
            raise IndexError()
        new_size = self.size + 1
        if new_size > self._values.size:
            new_values = np.empty(self.size + self._vector, dtype=self._dtype)
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
        if self._values.size - self.size > self._vector:
            new_values = np.empty(self.size - 1, dtype=self._dtype)
            for i in range(index):
                new_values[i] = self._values[i]
            for i in range(index + 1, self.size + 1):
                new_values[i - 1] = self._values[i]
            self._values = new_values
        else:
            for i in range(index, self.size):
                self._values[i] = self._values[i + 1]
        return self


if __name__ == "__main__":
    arr = VectorArray(int, 2)
    arr.add(0).add(1).add(2).remove(1).add(5).add(6, 0).remove(3)
    print(arr)
