from typing import NamedTuple, Any, TypeAlias
import numpy as np


class Node(NamedTuple):
    key: str
    value: Any


LinkedList: TypeAlias = list[Node]


class HashTable():
    _load_factor = 0.75
    _table_length = 10
    _cells_occupied = 0
    _values = np.array(10, dtype=object)

    def _get_hash(self, item: Any) -> int:
        return hash(item) % self._table_length

    def get(self):
        pass

    def put(self) -> None:
        pass

    def delete(self) -> None:
        pass


if __name__ == "__main__":
    ht = HashTable()
