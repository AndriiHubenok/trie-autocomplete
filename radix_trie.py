class RadixTrie:
    def __init__(self):
        self.children = {}
        self.frequency = 1
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        while len(word) > 0:
            match_key = None
            for key in node.children:
                if key[0] == word[0]:
                    match_key = key
                    break

            if match_key is None:
                new_node = RadixTrie()
                new_node.is_end = True
                node.children[word] = new_node
                return

            i = 0
            while i < len(match_key) and i < len(word) and match_key[i] == word[i]:
                i += 1

            if i < len(match_key):

                old_node = node.children.pop(match_key)

                split_node = RadixTrie()

                split_node.children[match_key[i:]] = old_node

                if i < len(word):
                    new_node = RadixTrie()
                    new_node.is_end = True
                    split_node.children[word[i:]] = new_node
                else:
                    split_node.is_end = True

                node.children[match_key[:i]] = split_node
                return

            else:
                node = node.children[match_key]
                word = word[i:]

                if len(word) == 0:
                    node.is_end = True
                    return

    def contains(self, word: str) -> bool:
        node = self

        while len(word) > 0:
            match_key = None
            for key in node.children:
                if key[0] == word[0]:
                    match_key = key
                    break

            if match_key is None:
                return False

            if word.startswith(match_key):
                word = word[len(match_key):]
                node = node.children[match_key]
            else:
                return False

        return node.is_end

    def nodes(self) -> int:
        count = 1

        for child in self.children.values():
            count += child.nodes()

        return count