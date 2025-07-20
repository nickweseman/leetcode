class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        substrings = set()
        def backtrack(index):
            if index == n:
                return 0
            result = 0
            for i in range(index, n):
                substring = s[index : i + 1]
                if substring not in substrings:
                    substrings.add(substring)
                    result = max(result, 1 + backtrack(i + 1)) # 1 for myself
                    substrings.remove(substring)
            return result
        return backtrack(0)