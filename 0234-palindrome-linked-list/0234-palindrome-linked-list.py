# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reversed(head:ListNode) -> ListNode:
            curr = head
            prev = None

            while curr:
                curr.next, prev, curr =  prev, curr, curr.next
            return prev
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = reversed(slow)
        slow = head

        while tail:
            if tail.val != slow.val:
                return False
            tail = tail.next
            slow = slow.next
            
        return True
        