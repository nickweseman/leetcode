class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = 0
        num_content = 0
        g.sort()
        s.sort()

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                num_content += 1
                i += 1
            j += 1
        return num_content