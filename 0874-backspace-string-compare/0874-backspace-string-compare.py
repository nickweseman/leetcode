class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:     
        def execute(st: str) -> str:
            keyboard = []
            i = 0

            while i < len(st):
                if st[i] == "#":
                    if keyboard:
                        keyboard.pop()
                else:
                    keyboard.append(st[i])
                i += 1
            return "".join(keyboard)
        return execute(s) == execute(t)