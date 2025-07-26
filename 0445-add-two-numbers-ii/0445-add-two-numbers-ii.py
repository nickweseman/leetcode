# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        result_head = None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr = ListNode(total % 10)
            curr.next = result_head
            result_head = curr
        return result_head
