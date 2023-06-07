class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        while c > 0 or a > 0 or b > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            if bit_c == 0:
                if bit_a == 1 and bit_b == 1:
                    flips += 2
                elif bit_a == 1 or bit_b == 1:
                    flips += 1
            else:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return flips

# TC : O(log(max(a, b, c))), where max(a, b, c) represents the maximum value among a, b, and c.
# SC : O(1) because it uses a constant amount of additional space to store the flips variable 
# and the temporary bit variables (bit_a, bit_b, bit_c). 