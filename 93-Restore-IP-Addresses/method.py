class Solution:
    def check(self, s):
        return s == str(int(s)) and int(s) <= 255

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if self.check(a) and self.check(b) and self.check(c) and self.check(d):
                        ans.append(f'{a}.{b}.{c}.{d}')
        return ans

## TC : O(n^3), where n is the length of the given string as it uses three nested loops to check for all possible combinations of IP addresses.
## SC : O(1), as it only uses a constant amount of variables to store the IP address segments and the final answer.
