class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def finalOutput(input):
            result = []
            for c in input:
                if c!= '#':
                    result.append(c)
                elif result:
                    result.pop()
            return "".join(result)
        return finalOutput(s) == finalOutput(t)

# TC : O(m+n), where m and n are the lengths of strings s and t, respectively. This is because we process each string once, and the time taken for processing is proportional to the length of the string.
# SC : O(m+n)