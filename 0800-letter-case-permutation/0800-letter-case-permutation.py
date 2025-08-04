class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        path = []
        result = []
        def backtrack(index):
            if index == n:
                result.append("".join(path))
                return
            if s[index].isalpha():
                path.append(s[index].upper())
                backtrack(index + 1)
                path.pop()
                path.append(s[index].lower())
                backtrack(index + 1)
                path.pop()
            else:
                path.append(s[index])
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result