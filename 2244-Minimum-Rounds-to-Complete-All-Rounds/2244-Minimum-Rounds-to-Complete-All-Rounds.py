class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency_count = {}
        for task in tasks:
            if task not in frequency_count:
                frequency_count[task] = 1
            else:
                frequency_count[task] += 1
        result = 0
        for difficulty, count in frequency_count.items():
            if count == 1:
                return -1
            elif count % 3 == 0:
                result += count // 3
            elif count % 3 == 1 or count % 3 == 2:
                result += count // 3 + 1

        return result
''' TC : O(n), where n is the length of the tasks array. This is because 
the solution has a single loop that iterates through the tasks array once to count 
the frequency of each difficulty level, and another loop that iterates through 
the frequency counts to calculate the minimum number of rounds required to complete all the tasks.'''
# SC : O(n), because it stores the frequency of each difficulty level in a dictionary, which has a size of n.
