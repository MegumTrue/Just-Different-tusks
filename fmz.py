class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word_end = True

    def display(self, node, prefix=""):
        if node.is_word_end:
            print(prefix)
        for char, child_node in node.children.items():
            self.display(child_node, prefix + char)

# Example usage
trie = Trie()
words = ["вкладыш","устойчивость", "устой", "уступ", "вкус"]

for word in words:
    trie.insert(word)

trie.display(trie.root, "")