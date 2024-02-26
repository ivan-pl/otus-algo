import typing as t


# Recursive
class Trie:
    def __init__(self):
        self._keys: list[t.Self] = [None for i in range(26)]
        self._is_final = False

    @staticmethod
    def _get_ind(s: str) -> int:
        return ord(s) - ord('a')

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self._is_final = True
            return

        ind = Trie._get_ind(word[0])
        if self._keys[ind]:
            self._keys[ind].insert(word[1:])
        else:
            next_trie = Trie()
            next_trie.insert(word[1:])
            self._keys[ind] = next_trie

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self._is_final
        ind = Trie._get_ind(word[0])
        if not self._keys[ind]:
            return False
        return self._keys[ind].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return self._is_final or any(v is not None for v in self._keys)
        ind = Trie._get_ind(prefix[0])
        if not self._keys[ind]:
            return False
        return self._keys[ind].startsWith(prefix[1:])


# Linear
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.keys: list[t.Self] = [None] * 26


class TrieR:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def _get_index(s: str) -> int:
        return ord(s) - ord('a')

    def insert(self, word: str) -> None:
        cur_node = self.root
        for w in word:
            ind = TrieR._get_index(w)
            if not cur_node.keys[ind]:
                cur_node.keys[ind] = TrieNode()
            cur_node = cur_node.keys[ind]
        cur_node.is_end = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for w in word:
            ind = TrieR._get_index(w)
            if not cur_node.keys[ind]:
                return False
            cur_node = cur_node.keys[ind]
        return cur_node.is_end

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for w in prefix:
            ind = TrieR._get_index(w)
            if not cur_node.keys[ind]:
                return False
            cur_node = cur_node.keys[ind]
        return True


if __name__ == "__main__":
    trie = TrieR()
    trie.insert("apple")
    print(trie.search("apple"))  # return True
    print(trie.search("app"))  # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))  # return True
