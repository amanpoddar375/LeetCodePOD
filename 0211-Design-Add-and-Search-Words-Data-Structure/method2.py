class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '$' in node
            if word[i] == '.':
                for child in node.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if word[i] not in node:
                    return False
                return dfs(node[word[i]], i + 1)

        return dfs(self.trie, 0)

      
'''
# Time Complexity:
# - addWord: O(n), where n is the length of the word being added
# - search:
#   * Worst-case: O(m * 26^k), where m is the maximum length of a word in the dictionary and k is the number of dots in the search word
#   * Best-case: O(k), where k is the number of dots in the search word (if the search word has no dots, the search is O(m))'''

'''
# Space Complexity: O(n * m), where n is the number of words in the dictionary and m is the maximum length of a word in the dictionary'''


