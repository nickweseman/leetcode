class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j = len(g) - 1, len(s) - 1
        content = 0

        while i >= 0 and j >= 0:
            if g[i] <= s[j]:
                content += 1
                j -= 1
            i -= 1
        return content
            
