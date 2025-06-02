class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
            else:
                if i == 0 or typed[j] != name[i - 1]:
                    return False
            j += 1
        while j < len(typed):
            if typed[j] != name[i - 1]:
                return False
            j += 1
        return i == len(name)