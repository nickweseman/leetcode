# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = lastUnique = head

        while current:
            if lastUnique.val != current.val:
                lastUnique.next = lastUnique = current  
            current = current.next
        if lastUnique:
            lastUnique.next = None
        return head