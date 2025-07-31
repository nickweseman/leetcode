class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_incoming = [False] * n
        for incoming, outgoing in edges:
            has_incoming[outgoing] = True
        result = []
        for i, node in enumerate(has_incoming):
            if not node:
                result.append(i)
        return result

