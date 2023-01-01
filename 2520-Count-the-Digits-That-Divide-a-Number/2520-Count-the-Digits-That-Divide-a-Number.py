class Solution:
    def countDigits(self, num: int) -> int:
        digit = list(str(num))
        count = 0
        for i in range (len(digit)):
            if num % int(digit[i]) == 0:
                count= count + 1
        return count
    
 ''' TC:  O(n), where n is the number of digits in the given number.
 This is because the for loop iterates through all the digits in the number and performs a constant time operation for each iteration. '''

''' SC: O(n), because we are creating a list of digits from the given number which takes up n space in memory. '''
