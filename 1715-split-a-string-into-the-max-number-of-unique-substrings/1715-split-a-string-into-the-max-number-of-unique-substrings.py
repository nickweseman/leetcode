class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        path = set()
        max_splits = 0
        n = len(s)
        def backtrack(index):
            nonlocal max_splits
            if index == n:
                print(path)
                max_splits = max(max_splits, len(path))
                return
            for i in range(index, n):
                substring = s[index: i + 1]
                if substring in path:
                    continue
                path.add(substring)
                backtrack(i + 1)
                path.remove(substring)
        backtrack(0)
        return max_splits