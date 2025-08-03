class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py
        for i in range(len(s1)):
            s1_idx = ord(s1[i]) - ord('a')
            s2_idx = ord(s2[i]) - ord('a')
            union(s1_idx, s2_idx)
        result = []
        for c in baseStr:
            c_idx = ord(c) - ord('a')
            p_idx = find(c_idx)
            p = chr(p_idx + ord('a'))
            result.append(p)
        return "".join(result)