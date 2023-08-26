class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  
        
        current_end = float('-inf')  
        longest_chain = 0
        
        for pair in pairs:
            if pair[0] > current_end:
                longest_chain += 1
                current_end = pair[1]
        
        return longest_chain

# TC :  O(nlogn), where n is the number of pairs
# SC : O(1)