class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = len(g) - 1, len(s) - 1
        happy = 0
        
        g.sort()
        s.sort()
        
        while i >= 0 and j >= 0:
            if g[i] <= s[j]:
                j -= 1
                happy += 1
            i -= 1
        return happy


        