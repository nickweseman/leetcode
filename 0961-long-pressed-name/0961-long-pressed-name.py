class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        need = scan = 0
        ignore_char = None

        while need < len(name) and scan < len(typed):
            if name[need] == typed[scan]:
                need += 1
                ignore_char = typed[scan]
            else:
                if typed[scan] != ignore_char:
                    return False
            scan += 1
        while scan < len(typed):
            if typed[scan] != ignore_char:
                return False
            scan += 1
        return need == len(name)
        