class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def execute(x: str) -> str:
            i = 0
            output = []
            while i < len(x):
                if x[i] != "#":
                    output.append(x[i])
                else:
                    if output:
                        output.pop()
                i += 1
            return "".join(output)
            
        return execute(s) == execute(t)

        