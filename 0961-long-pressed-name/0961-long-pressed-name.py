class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                if i > 0 and name[i - 1] == typed[j]:
                    j += 1
                else:
                    return False
            else:
                i += 1
                j += 1
        while j < len(typed):
            if name[i - 1] != typed[j]:
                if i > 0 and name[i - 1] == typed[j]:
                    j += 1
                else:
                    return False
            else:
                j += 1
        return i == len(name)