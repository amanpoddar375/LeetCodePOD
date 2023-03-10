# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        
        self.head = head

    def getRandom(self) -> int:
        count = 0
        curr = self.head
        res = None
        while curr:
            count += 1
            if random.randint(1, count) == 1:
                res = curr.val
            curr = curr.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


''' # TC (of __init__ ) : O(n) since it iterates through the entire linked list to count the number of nodes.

    # TC (getRandom) : O(n) in the worst case since it might have to traverse the entire linked list to find a random node. '''

''' # SC (of the Solution class) : O(n) to store the linked list.'''
