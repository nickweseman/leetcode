class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = []
        low, high = 0, len(s)

        for c in s:
            if c == "I":
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1
        perm.append(low)
        return perm
