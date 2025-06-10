# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(h: ListNode) -> ListNode:
            curr = h
            prev = None
            while curr:
                curr.next, curr, prev = prev, curr.next, curr
            return prev
        
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = reverse(slow)

        while tail:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True
        
        