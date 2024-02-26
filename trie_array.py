import typing as t


class TrieNode:
    def __init__(self):
        self.value: t.Any = None
        self.keys: list[t.Self | None] = [None for _ in range(26)]

    def __repr__(self) -> str:
        return f'TrieNode({self.value=}, {self.keys=})'


class Trie:
    def __init__(self):
        self._root = TrieNode()

    @staticmethod
    def _get_ind(char: str) -> int:
        return ord(char) - ord('a')

    def __getitem__(self, key: str) -> t.Any:
        """Returns None if not found"""
        cur_node = self._root
        for char in key:
            ind = Trie._get_ind(char)
            if not cur_node.keys[ind]:
                return
            cur_node = cur_node.keys[ind]
        return cur_node.value

    def __setitem__(self, key: str, value: t.Any) -> None:
        cur_node = self._root
        for char in key:
            ind = Trie._get_ind(char)
            if not cur_node.keys[ind]:
                cur_node.keys[ind] = TrieNode()
            cur_node = cur_node.keys[ind]
        cur_node.value = value

    def __delitem__(self, key: str) -> t.Any:
        cur_node = self._root
        node_stack: list[TrieNode] = [cur_node]
        for char in key:
            ind = Trie._get_ind(char)
            if not cur_node.keys[ind]:
                return
            cur_node = cur_node.keys[ind]
            node_stack.append(cur_node)
        value = cur_node.value
        cur_node.value = None

        if not all(v is None for v in cur_node.keys):
            return value
        for node, char in reversed(list(zip(node_stack, key))):
            ind = Trie._get_ind(char)
            node.keys[ind] = None
            if node.value or any(v is not None for v in node.keys):
                return value
        return value

    def __repr__(self) -> str:
        return self._root.__repr__()


if __name__ == "__main__":
    trie = Trie()
    trie['as'] = 111
    trie['asdf'] = 222
    print(trie['as'])  # 111
    print(trie['asdf'])  # 222
    del trie['asdf']
    print(trie['asdf'])  # None
    print(trie['as'])  # 111
