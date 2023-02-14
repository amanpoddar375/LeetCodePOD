class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal1 = int(a,2)
        decimal2 = int(b,2)
        add = decimal1 + decimal2
        return bin(add)[2:]
