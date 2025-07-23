# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        cur_position = 1
        prev = None
        curr = head
        while curr.next and cur_position < left:
            prev = curr
            curr = curr.next
            cur_position += 1
        node_before_reverse = prev
        save_this_curr = curr
        while curr and cur_position <= right:
            curr.next, curr, prev = prev, curr.next, curr
            cur_position += 1
        save_this_curr.next = curr
        if node_before_reverse:
            node_before_reverse.next = prev
        else:
            head = prev
        return head