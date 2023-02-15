class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        integer = 0
        for i in range(len(num)):
            integer += num[i] * (10 ** (len(num) - i - 1))
        sum = integer + k
        if sum == 0:
            return [0]
        res = []
        while sum > 0:
            res.append(sum % 10)
            sum //= 10
        return res[::-1]
