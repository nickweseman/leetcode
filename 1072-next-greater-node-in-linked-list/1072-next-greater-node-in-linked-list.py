# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        answer = [0] * len(values)
        stack = []
        for i, num in enumerate(values):
            while stack and values[stack[-1]] < num:
                answer[stack.pop()] = num
            stack.append(i)
        return answer