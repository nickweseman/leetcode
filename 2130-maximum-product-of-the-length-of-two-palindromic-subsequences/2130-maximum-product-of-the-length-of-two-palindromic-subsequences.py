class Solution:
    def maxProduct(self, s: str) -> int:
        s1 = []
        s2 = []
        n = len(s)
        max_product = -math.inf
        def backtrack(index):
            nonlocal max_product
            if index == n:
                if s1 == s1[::-1] and s2 == s2[::-1]:
                    max_product = max(max_product, len(s1) * len(s2))
                return
            s1.append(s[index])
            backtrack(index + 1)
            s1.pop()
            s2.append(s[index])
            backtrack(index + 1)
            s2.pop()
            backtrack(index + 1)
        backtrack(0)
        return max_product

