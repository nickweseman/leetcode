class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = []
        incoming = set()
        for edge in edges:
            incoming.add(edge[1])
        for i in range(n):
            if i not in incoming:
                result.append(i)
        return result