# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reversed(head: ListNode) -> ListNode:
            curr = head
            prev = None

            while curr:
                tempNode = curr.next
                curr.next = prev
                prev = curr
                curr = tempNode

            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = reversed(slow)

        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True


        