class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 0;
        temp = num;
        rightdigitcount = -1;
        while temp > 0:
            if temp % 10 == 6:
                rightdigitcount = i
            temp = temp//10
            i+=1
        if (rightdigitcount == -1): 
            return num;
        else:
            return num + (3 * (10**rightdigitcount));
