class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        output = []

        for c in s:
            if c == "I":
                output.append(left)
                left += 1
            else:
                output.append(right)
                right -= 1
        output.append(left)
        return output