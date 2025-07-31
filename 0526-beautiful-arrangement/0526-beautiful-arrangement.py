class Solution:
    def countArrangement(self, n: int) -> int:
        num_beautiful = 0
        used = [False] * (n + 1)
        def backtrack(index):
            nonlocal num_beautiful
            if index == n + 1:
                num_beautiful += 1
                return
            for i in range(1, n + 1):
                if (index % i == 0 or i % index == 0) and not used[i]:
                    used[i] = True
                    backtrack(index + 1)
                    used[i] = False
        backtrack(1)
        return num_beautiful