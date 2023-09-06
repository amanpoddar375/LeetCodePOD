# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the size of each part and the number of larger parts
        part_size = length // k
        larger_parts = length % k
        
        result = []
        current = head
        for i in range(k):
            result.append(current)
            part_length = part_size + (1 if i < larger_parts else 0)
            
            # Split the linked list into parts
            for j in range(part_length - 1):
                if current:
                    current = current.next
            
            # Disconnect the current part from the rest of the list
            if current:
                temp = current.next
                current.next = None
                current = temp
        
        return result

# TC : O(n), where n represent the number of input linked list
# SC : O(k)