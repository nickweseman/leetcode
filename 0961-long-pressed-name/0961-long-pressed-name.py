class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        need = scan = 0
        ignore_char = 0

        while need < len(name) and scan < len(typed):
            if name[need] == typed[scan]:
                need += 1
                ignore_char = ord(typed[scan])
            else:
                if ord(typed[scan]) != ignore_char:
                    return False
            scan += 1
        while scan < len(typed):
            if ord(typed[scan]) != ignore_char:
                return False
            scan += 1
        return need == len(name)
        