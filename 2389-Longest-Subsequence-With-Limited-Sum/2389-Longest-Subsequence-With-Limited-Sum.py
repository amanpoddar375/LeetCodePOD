class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        for query in queries:
            count = 0
            total = 0
            for num in nums:
                total += num
                count += 1
                if total > query:
                    count -= 1
                    break
            result.append(count)
        return result
