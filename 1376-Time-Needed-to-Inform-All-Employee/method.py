class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create a dictionary to represent the tree structure
        tree = defaultdict(list)
        for employee, manager_id in enumerate(manager):
            tree[manager_id].append(employee)

        # Helper function to calculate the time needed to inform all employees starting from the given employee
        def calculateTime(employee):
            if not tree[employee]:  # If the employee has no subordinates, informTime is 0
                return 0
            max_time = 0
            for subordinate in tree[employee]:
                max_time = max(max_time, calculateTime(subordinate))
            return informTime[employee] + max_time

        # Start the calculation from the head of the company
        return calculateTime(headID)
