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

    def fuzzy(self, query: str, k: int) -> list:
        results = []
        first_row = list(range(len(query) + 1))

        if self.is_end and first_row[-1] <= k:
            results.append(("", first_row[-1]))

        for char, child in self.children.items():
            self._fuzzy_dfs(child, char, char, first_row, query, k, results)

        return results

    def _fuzzy_dfs(self, node, char, current_word, prev_row, query, k, results):
        columns = len(query) + 1
        curr_row = [prev_row[0] + 1]

        for i in range(1, columns):
            insert_cost = curr_row[i - 1] + 1
            delete_cost = prev_row[i] + 1
            replace_cost = prev_row[i - 1] + (0 if query[i - 1] == char else 1)

            curr_row.append(min(insert_cost, delete_cost, replace_cost))

        if node.is_end and curr_row[-1] <= k:
            results.append((current_word, curr_row[-1]))

        if min(curr_row) <= k:
            for next_char, child in node.children.items():
                self._fuzzy_dfs(child, next_char, current_word + next_char, curr_row, query, k, results)

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
