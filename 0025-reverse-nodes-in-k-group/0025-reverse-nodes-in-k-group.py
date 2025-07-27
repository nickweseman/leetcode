# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def k_nodes_exist(head):
            for _ in range(k):
                head = head.next
                if not head:
                    return False
            return True
        dummy = ListNode(0, next=head)
        node_before_reversal = dummy
        reverse_tail = head
        while k_nodes_exist(node_before_reversal):
            prev = None
            curr = node_before_reversal.next
            for _ in range(k):
                curr.next, curr, prev = prev, curr.next, curr
            node_before_reversal.next = prev
            reverse_tail.next = curr
            node_before_reversal = reverse_tail
            reverse_tail = curr
        return dummy.next
        