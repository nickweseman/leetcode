class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def execute(ss: str) -> str:
            i: int = 0
            output: list[str] = []

            while i < len(ss):
                if ss[i] != "#":
                    output.append(ss[i])
                else:
                    if output:
                        output.pop()
                i += 1
            return "".join(output)
        
        return execute(s) == execute(t)

        