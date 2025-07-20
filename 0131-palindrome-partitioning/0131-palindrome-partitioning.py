class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        path = []
        result = []
        def backtrack(index):
            if index == n:
                result.append(path.copy())
                return
            for i in range(index, n):
                substring = s[index : i + 1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)
        return result