# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        cur_position = 1
        prev = dummy
        curr = head
        while cur_position < left:
            prev = curr
            curr = curr.next
            cur_position += 1
        node_before_reversal = prev
        reversal_tail = curr
        while cur_position <= right:
            curr.next, curr, prev = prev, curr.next, curr
            cur_position += 1
        reversal_tail.next = curr
        node_before_reversal.next = prev
        return dummy.next