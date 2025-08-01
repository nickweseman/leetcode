class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        def backtrack(index):
            if index == n + 1:
                if len(path) == k:
                    result.append(path.copy())
                return
            if len(path) > k:
                return
            path.append(index)
            backtrack(index + 1)
            path.pop()
            backtrack(index + 1)
        backtrack(1)
        return result