class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = 0
        g.sort()
        s.sort()
        happy = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1 
                happy += 1
            j += 1
        return happy