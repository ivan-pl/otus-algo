from typing import NamedTuple, Any, TypeAlias
import numpy as np


class Node(NamedTuple):
    key: Any
    value: Any


LinkedList: TypeAlias = list[Node]


class HashTable():
    _load_factor = 0.75
    _table_length = 10
    _cells_occupied = 0
    _values = np.empty(10, dtype=object)  # array of LinkedLists

    def _get_hash(self, key: Any) -> int:
        return hash(key) % self._table_length

    def get(self):
        pass

    def put(self, key: Any, value: Any) -> None:
        index = self._get_hash(key)

        new_node = Node(key, value)
        if not self._values[index]:
            self._values[index] = [new_node]
            return

        for i, node in enumerate(self._values[index]):
            if node.key == key:
                self._values[index][i] = new_node
                return
        self._values[index].append(new_node)

    def delete(self) -> None:
        pass


if __name__ == "__main__":
    ht = HashTable()
    ht.put('asd', 1)
    ht.put('qwe', 2)
    ht.put('asd', 4)
    print(ht)
