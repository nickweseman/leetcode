# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node) -> ListNode:
            curr = node
            prev = None
            while curr:
                curr.next, curr, prev = prev, curr.next, curr
            return prev
        
        if not head:
            return True
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = reverse(slow)

        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True