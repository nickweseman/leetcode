class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        path = []
        def backtrack(index):
            if len(path) == len(s):
                result.append("".join(path))
                return
            char = s[index]
            if char.isalpha():
                path.append(char.lower())
                backtrack(index + 1)
                path.pop()
                path.append(char.upper())
                backtrack(index + 1)
                path.pop()
            else:
                path.append(char)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result