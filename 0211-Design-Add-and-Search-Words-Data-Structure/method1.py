class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word)

    def _search(self, node, word):
        if not word:
            return node.is_end_of_word

        c = word[0]
        if c == ".":
            for child in node.children.values():
                if self._search(child, word[1:]):
                    return True
            return False

        if c not in node.children:
            return False

        return self._search(node.children[c], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

'''# Time Complexity:
# - addWord: O(n), where n is the length of the word being added
# - search:
#   Worst-case: O(m * 26^k), where m is the maximum length of a word in the dictionary and k is the number of dots in the search word
#   Best-case : O(k), where k is the number of dots in the search word 
              (if the search word has no dots, the search is O(m))'''

'''# Space Complexity: O(n * m), where n is the number of words in the dictionary and m is the maximum length of a word in the dictionary'''
