class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def backtrack(index, open_count, closed_count):
            if index ==  2 * n:
                result.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(index + 1, open_count + 1, closed_count)
                path.pop()
            if open_count > closed_count:
                path.append(")")
                backtrack(index + 1, open_count, closed_count + 1)
                path.pop()
        backtrack(0, 0, 0)
        return result