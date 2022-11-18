class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_list = [1]                   #initializing the list with element 1
        nextMulfact_2, nextMulfact_3, nextMulfact_5 = 0, 0, 0   #initally multiplication is done with 0 to get 1
        
        while len(ugly_list) < n:
        
            nextUgly_2 = ugly_list[nextMulfact_2] * 2
            nextUgly_3 = ugly_list[nextMulfact_3] * 3
            nextUgly_5 = ugly_list[nextMulfact_5] * 5
            
            ugly_min = min(nextUgly_2, nextUgly_3, nextUgly_5)
            
            ugly_list.append(ugly_min)
            
            if ugly_min == nextUgly_2:
                nextMulfact_2 +=1
            if ugly_min == nextUgly_3:
                nextMulfact_3 +=1
            if ugly_min == nextUgly_5:
                nextMulfact_5 +=1
            
        return ugly_list[-1]           #returning the last element of ugly list
    
    #Time Complexity: O(N)
    #Space complexity : O(N)