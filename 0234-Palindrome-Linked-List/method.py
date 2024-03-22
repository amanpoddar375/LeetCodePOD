# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []  # Initialize an empty list
        current = head  # Start from the head of the linked list

        # Traverse the linked list and append each node's value to the list
        while current:
            vals.append(current.val)
            current = current.next

        # Check if the list is equal to its reverse
        return vals == vals[::-1]

# TC :O(n), where n is the length of the linked list, because it needs to traverse the entire linked list once to store the values in the list.
# SC : O(n) because it uses a list to store all the values of the linked list.