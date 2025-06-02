class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ran = list(range(len(s) + 1))
        left, right = 0, len(ran) - 1
        output = []

        for c in s:
            if c == "I":
                output.append(ran[left])
                left += 1
            else: # c == "D"
                output.append(ran[right])
                right -= 1
        output.append(ran[left])
        return output
        