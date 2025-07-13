import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return
            for i in range(start, n + 1):
                if (n - i + 1) < (k - len(combination)): # purely optional pruning step
                    break
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()
        backtrack(1, [])
        return result