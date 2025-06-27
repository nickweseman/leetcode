class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        n = len(s)
        ss = list(s)

        for i in reversed(range(n)):
            total_shifts += shifts[i]

            diff = ord(ss[i]) - ord('a')
            diff = (diff + total_shifts) % 26
            ss[i] = chr(diff + ord('a'))
        return "".join(ss)