class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        KEYS = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        result = []
        path = []
        def backtrack(index):
            if index == len(digits):
                if len(path) > 0:
                    result.append("".join(path))
                return
            for c in KEYS[int(digits[index])]:
                path.append(c)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result
        