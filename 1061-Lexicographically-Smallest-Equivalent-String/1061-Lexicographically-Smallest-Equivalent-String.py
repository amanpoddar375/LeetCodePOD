class Solution:
    def find(self, i: int, parent: List[int]) -> int:
        if i == parent[i]:
            return i
        return self.find(parent[i], parent)
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            x = self.find(ord(s1[i]) - ord('a'), parent)
            y = self.find(ord(s2[i]) - ord('a'), parent)
            if x != y:
                if x < y:
                    parent[y] = x
                else:
                    parent[x] = y
        res = ""
        for ch in baseStr:
            res += chr(self.find(ord(ch) - ord('a'), parent) + ord('a'))
        return res

''' ## TC : O(n) where n is the length of the input strings s1 and s2. 
    ## SC : O(1) because it only uses a constant amount of extra space 
    (i.e. the "parent" list and the "res" string) regardless of the size of the input.'''
''' TC is O(n), because the method iterates through the characters of both strings once, and for each pair of characters, 
it performs a constant amount of work (i.e. calling the "find" function and updating the "parent" list) which takes constant time.
Also, the find method is called inside the smallestEquivalentString method, and the complexities of the find method are added to the 
complexities of smallestEquivalentString method.''' 
