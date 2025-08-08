# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def contains_k_nodes(node):
            for _ in range(k):
                node = node.next
                if not node:
                    return False
            return True
        dummy = ListNode(0, next=head)
        node_before_reversal = dummy
        while contains_k_nodes(node_before_reversal):
            reverse_tail = node_before_reversal.next
            prev = None
            curr = reverse_tail
            for _ in range(k):
                curr.next, curr, prev = prev, curr.next, curr
            node_before_reversal.next = prev
            reverse_tail.next = curr
            node_before_reversal = reverse_tail
        return dummy.next