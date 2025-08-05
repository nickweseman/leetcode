class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        n = len(s)
        def backtrack(index):
            if n == index:
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