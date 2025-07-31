class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        inter = set(edges[0]) & set(edges[1])
        return inter.pop()