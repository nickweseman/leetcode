class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = []

        for c in s:
            if c == "(":
                if depth:
                    result.append(c)
                depth += 1
            else:
                depth -= 1
                if depth:
                    result.append(c)
        return "".join(result)