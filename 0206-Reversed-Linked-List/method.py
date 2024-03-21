# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        return prev
    
# TC : O(n), where n is the number of nodes in the linked list, as we traverse the list only once. 
# SC : O(1) since we use a constant amount of extra space for the pointers prev, curr, and next_node.