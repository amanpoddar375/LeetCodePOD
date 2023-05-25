class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
    
# TC : O(n log k), where n is the length of the nums list and k is the desired number of most frequent elements.
# SC : O(max(n, k))