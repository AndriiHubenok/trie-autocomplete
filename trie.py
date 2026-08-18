class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]

        node.is_end = True

    def contains(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def size(self) -> int:
        count = 1 if self.is_end else 0

        for child in self.children.values():
            count += child.size()

        return count