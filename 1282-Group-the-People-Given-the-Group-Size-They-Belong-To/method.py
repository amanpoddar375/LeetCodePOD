class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = {}  
        result = []      
        
        for i, size in enumerate(groupSizes):
            if size not in group_dict:
                group_dict[size] = []  
            
            group_dict[size].append(i)  
            
            if len(group_dict[size]) == size:
                result.append(group_dict[size])  
                group_dict[size] = []  
            
        return result

# TC : O(n), where n is the length of groupsize list
# SC : O(n)