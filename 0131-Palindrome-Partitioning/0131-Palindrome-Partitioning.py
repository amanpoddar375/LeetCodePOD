class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def recursion(start: int, path: List[str], ans: List[List[str]]):
            if start == len(s):
                ans.append(path)
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    recursion(i+1, path+[s[start:i+1]], ans)

        ans = []
        recursion(0, [], ans)
        return ans

## TC : O(2^n * n), the TC of the recursion is O(2^n) and the TC of checking if a substring is a palindrome is O(n)
## SC : O(n), as we need to store the current partition path, which at worst case scenario can have n elements in it.
