class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
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
            if index == n:
                result.append("".join(path))
                return
            for letter in KEYS[int(digits[index])]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result