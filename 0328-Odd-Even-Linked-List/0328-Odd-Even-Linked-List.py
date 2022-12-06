# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or  not head.next or not head.next.next:
            return head
        op = head
        ep = head.next
        #declaring startofep as list of even nodes
        startofep = head.next
        while op.next and ep.next:
            op.next = ep.next
            ep.next = op.next.next
            op = op.next
            ep = ep.next
        #add the even nodes list into the odd nodes list
        op.next = startofep
        return head
