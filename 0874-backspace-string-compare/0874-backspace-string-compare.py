class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def execute(input):
            stack = []
            for c in input:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
        return execute(s) == execute(t)