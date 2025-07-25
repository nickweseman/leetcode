# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def k_nodes_exist(node) -> bool:
            for _ in range(k):
                node = node.next
                if not node:
                    return False
            return True
        dummy = ListNode(0, head)
        node_before_reversal = dummy
        while k_nodes_exist(node_before_reversal):
            reversal_tail = node_before_reversal.next
            prev = None
            curr = reversal_tail
            for _ in range(k):
                curr.next, curr, prev = prev, curr.next, curr
            node_before_reversal.next = prev
            reversal_tail.next = curr
            node_before_reversal = reversal_tail
        return dummy.next