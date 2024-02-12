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

    def get(self, key: Any) -> Any:
        index = self._get_hash(key)
        if not self._values[index]:
            raise KeyError()

        for node in self._values[index]:
            if node.key == key:
                return node.value

        raise KeyError()

    def put(self, key: Any, value: Any) -> None:
        index = self._get_hash(key)

        new_node = Node(key, value)
        if not self._values[index]:
            self._values[index] = [new_node]
            self._cells_occupied += 1
            if self._cells_occupied / self._table_length > self._load_factor:
                self._rehash()
            return

        for i, node in enumerate(self._values[index]):
            if node.key == key:
                self._values[index][i] = new_node
                return
        self._values[index].append(new_node)

    def delete(self, key: Any) -> None:
        index = self._get_hash(key)
        if not self._values[index]:
            return

        for i, node in enumerate(self._values[index]):
            if node.key == key:
                self._values[index].pop(i)
                if not self._values[index]:
                    self._cells_occupied -= 1
                return

    def _rehash(self) -> None:
        self._table_length *= 2
        self._cells_occupied = 0
        old_values = self._values
        self._values = np.empty(self._table_length, dtype=object)
        for linked_list in old_values:
            if not linked_list:
                continue

            for node in linked_list:
                self.put(**node)


if __name__ == "__main__":
    ht = HashTable()
    ht.put('asd', 1)
    ht.put('qwe', 2)
    ht.put('asd', 4)
    print(ht)
