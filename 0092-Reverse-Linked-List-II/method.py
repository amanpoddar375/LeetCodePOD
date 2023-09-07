# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_left = dummy
        
        # move to the left position
        for _ in range(left - 1):
            prev_left = prev_left.next
        
        # initialize pointers for reversal
        prev = None
        current = prev_left.next
        
        # reverse the portion from left to right
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # connect the reversed portion back to the list
        prev_left.next.next = current
        prev_left.next = prev
        
        return dummy.next

# TC : O(n), where n is the number of node in the linked list
# SC : O(1)