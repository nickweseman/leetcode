# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                min_heap.append((node.val, i, node))
        heapq.heapify(min_heap)
        while min_heap:
            _, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if curr.next:
                heapq.heappush(min_heap, (curr.next.val, i, curr.next))
        return dummy.next