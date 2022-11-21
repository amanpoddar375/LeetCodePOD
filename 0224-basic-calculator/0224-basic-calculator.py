class Solution:
    def calculate(self, s: str) -> int:
        sum, sign, num, stack = 0, 1, 0, []
        
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in ["+", "-"]:
                sum+= sign * num
                num = 0
                sign =[-1,1][char == "+"]
            elif char == "(" :
                stack.append(sum)
                stack.append(sign)
                sign, sum = 1, 0
            elif char == ")":
                sum+= sign * num
                sum*= stack.pop()
                sum+= stack.pop()
                num = 0
        return sum + num * sign