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
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = reverse(slow)

        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
        