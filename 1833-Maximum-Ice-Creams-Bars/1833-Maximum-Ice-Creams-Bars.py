class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for i in range(0, len(costs)):
            if coins - costs[i] >= 0 :
                ans+=1
                coins -= costs[i]
            else:
                break
        return ans
      
''' TC : O(n * log(n)), where n is the number of elements in the costs vector. 
This is because the sort() function has a time complexity of O(n * log(n)), 
and the for loop that iterates over the costs vector has a time complexity of O(n).''' 

''' SC : O(1), because this solution does not use any additional data structures 
to store intermediate results. It only modifies the variables num and coins, which have a constant size. '''
