import numpy as np
from base import BaseArray


class SingleArray(BaseArray):
    def remove(self, index):
        if index >= self.size:
            return self
        new_values = np.empty(self.size - 1, dtype=self._dtype)
        for i in range(index):
            new_values[i] = self._values[i]
        for i in range(index + 1, self.size):
            new_values[i - 1] = self._values[i]
        self._values = new_values
        self.size -= 1
        return self

    def add(self, item, index=None):
        if index is None:
            index = self.size
        if index > self.size:
            raise IndexError()
        new_size = self.size + 1
        new_values = np.empty(new_size, dtype=self._dtype)
        for i in range(index):
            new_values[i] = self._values[i]
        new_values[index] = item
        for i in range(index + 1, new_values.size):
            new_values[i] = self._values[i - 1]
        self._values = new_values
        self.size = new_size
        return self

    def __repr__(self):
        return str(self._values)


if __name__ == "__main__":
    arr = SingleArray(int)
    arr.add(0).add(1).add(2).remove(1).add(5).add(6, 0).remove(3)
    print(arr)
