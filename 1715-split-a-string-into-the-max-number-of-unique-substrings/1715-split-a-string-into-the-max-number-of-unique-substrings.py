class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        substrings = set()
        n = len(s)
        max_splits = -math.inf
        def backtrack(index):
            nonlocal max_splits
            if index == n:
                max_splits = max(max_splits, len(substrings))
                return
            for i in range(index, n):
                substring = s[index : i + 1]
                if substring not in substrings:
                    substrings.add(substring)
                    backtrack(i + 1)
                    substrings.remove(substring)
        backtrack(0)
        return max_splits