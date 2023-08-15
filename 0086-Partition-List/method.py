# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode()
        after_head = ListNode()
        before = before_head
        after = after_head
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            
            current = current.next
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next

# TC : O(n), where n is the number of nodes in the original linked list.
# SC : O(1)