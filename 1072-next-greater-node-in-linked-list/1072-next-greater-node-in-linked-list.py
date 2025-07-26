# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        result = []
        values = []
        while head:
            values.append(head.val)
            head = head.next
        n = len(values)
        result = [0] * n
        for i, num in enumerate(values):
            while stack and values[stack[-1]] < num:
                result[stack.pop()] = num
            stack.append(i)
        return result
        