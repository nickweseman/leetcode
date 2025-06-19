class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def execute(ss: str = "") -> str:
            stack = []
            for c in ss:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        return execute(s) == execute(t)