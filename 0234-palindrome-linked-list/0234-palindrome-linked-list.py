# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                curr.next, curr, prev = prev, curr.next, curr
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
        