class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        indices_of_value = defaultdict(list)
        for i in range(n):
            indices_of_value[arr[i]].append(i)
        visited = set()
        visited.add(0)
        q = deque([0])
        step = 0
        while q:
            for i in range(len(q)):
                curr_idx = q.popleft()
                if curr_idx == n - 1:
                    return step
                next_indices = [curr_idx - 1, curr_idx + 1] + indices_of_value[arr[curr_idx]]
                for idx in next_indices:
                    if 0 <= idx < n and idx not in visited:
                        visited.add(idx)
                        q.append(idx)
                indices_of_value[arr[curr_idx]].clear()
            step += 1
        return -1

'''# TC : O(n), where n is the length of the input array. The worst-case scenario is when all the elements in the array are the same. In this case, we need to visit all the elements at least once to compute the minimum number of steps required to reach the last index.'''

'''# SC : O(n) as we are using a queue to perform the BFS traversal and a dictionary to store the indices of each element in the array.'''
