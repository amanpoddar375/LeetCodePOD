class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        pq = []
        res = []
        max_enq_time = 0
        i = 0
        while len(res) < len(tasks):
            if i < len(tasks) and not pq:
                max_enq_time = max(max_enq_time, tasks[i][0])
            while i < len(tasks) and max_enq_time >= tasks[i][0]:
                heapq.heappush(pq, [tasks[i][1], tasks[i][2]])
                i += 1
            x = heapq.heappop(pq)
            max_enq_time = min(1000000000, x[0] + max_enq_time)
            res.append(x[1])
        return res
      
#TC: O(n * log(n))
#The for loop in the beginning takes O(n) time to run, as it iterates through all the tasks.
#The sort function takes O(n * log(n)) time to run, as it sorts the tasks based on their start times and durations.
#The while loop runs for a maximum of n iterations, as it adds one element to the result list per iteration.
#Inside the while loop, the heapq functions take O(log(n)) time to run, as they insert and pop elements from the heap.
#Therefore, the overall time complexity of the solution is O(n * log(n))

#SC: O(n), as it uses a heap to store the tasks that are waiting to be processed.
#The size of the heap will never exceed n, as it only stores tasks that have arrived but have not yet been processed
