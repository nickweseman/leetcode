class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        scan = need = 0

        while need < len(name) and scan < len(typed):
            if name[need] == typed[scan]:
                need += 1
            else:
                if need == 0 or typed[scan] != name[need-1]:
                    return False
            scan += 1
        while scan < len(typed):
            if typed[scan] != name[need-1]:
                return False
            scan += 1
        return need == len(name)