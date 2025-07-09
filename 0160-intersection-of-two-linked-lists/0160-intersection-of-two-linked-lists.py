# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_set = set()
        while headA:
            a_set.add(headA)
            headA = headA.next
        
        while headB:
            if headB in a_set:
                return headB
            headB = headB.next