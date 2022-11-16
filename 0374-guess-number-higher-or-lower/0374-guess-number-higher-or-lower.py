# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        l = 1
        h = n
        while(l<=h):
            m =(l+h)//2
            if(guess(m)==-1):
                h = m -1 
            elif(guess(m)==1):
                l = m+1
            else:
                return m
        return int(l)