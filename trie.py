from pygments.lexer import words


class Trie:
    def __init__(self):
        self.children = {}
        self.frequency = 1
        self.is_end = False

    def insert(self, word: str, frequency=1) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
                node.children[char].frequency = frequency
            # else:
            #     node.children[char].frequency += frequency
            node = node.children[char]

        node.is_end = True

    def contains(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def delete(self, word: str):
        node = self
        letters_nodes = [node]
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            letters_nodes.append(node)

        letters_nodes.reverse()
        index = len(word) - 1

        for n in letters_nodes[1:]:
            del n.children[word[index]]
            n.frequency -= 1

            if len(n.children) > 0:
                return True
            else:
                n.is_end = True

            index -= 1

        return True

    def suggest(self, prefix: str, k: int) -> list:
        node = self
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self.dfs(node, prefix, results)
        results.sort(key=lambda x: (-x.freq, x.word))
        return results[:k]

    def size(self) -> int:
        count = 1 if self.is_end else 0

        for child in self.children.values():
            count += child.size()

        return count

    def freq(self, word) -> int:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.frequency

    def nodes(self) -> int:
        count = 1

        for child in self.children.values():
            count += child.nodes()

        return count

    def prefix(self, word):
        node = self
        prefix = ''

        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
            prefix += char

        results = []
        self.dfs(node, prefix, results)
        return results

    def dfs(self, node, prefix, words):
        if node.is_end:
            words.append(WordWithFreq(prefix, node.frequency))

        for char, child in node.children.items():
            self.dfs(child, prefix + char, words)

class WordWithFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __str__(self):
        return f'{self.word}({self.freq})'
