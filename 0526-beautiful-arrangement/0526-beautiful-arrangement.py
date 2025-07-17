class Solution:
    def countArrangement(self, n: int) -> int:
        total = 0
        used = [False] * (n + 1)
        def backtrack(index):
            nonlocal total
            if index == n + 1:
                total += 1
                return
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if index % i == 0 or i % index == 0:
                    used[i] = True
                    backtrack(index + 1)
                    used[i] = False
        backtrack(1)
        return total
            