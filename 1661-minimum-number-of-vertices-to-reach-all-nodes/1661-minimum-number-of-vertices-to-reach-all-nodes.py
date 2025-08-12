class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degrees = collections.defaultdict(int)
        for in_edge, out_edge in edges:
            in_degrees[out_edge] += 1
        result = []
        for i in range(n):
            if in_degrees[i] == 0:
                result.append(i)
        return result
        