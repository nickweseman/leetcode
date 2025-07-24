# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr_position = 1
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr_position < left:
            prev = curr
            curr = curr.next
            curr_position += 1
        node_before_reversal = prev
        reversal_tail = curr
        prev = None
        while curr_position <= right:
            curr.next, curr, prev = prev, curr.next, curr
            curr_position += 1
        node_before_reversal.next = prev
        reversal_tail.next = curr
        return dummy.next
