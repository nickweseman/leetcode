class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(index):
            if index > n + 1:
                return
            if len(path) == k:
                result.append(path.copy())
                return
            path.append(index)
            backtrack(index + 1)
            path.pop()
            backtrack(index + 1)
        backtrack(1)
        return result