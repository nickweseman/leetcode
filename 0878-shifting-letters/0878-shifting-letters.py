class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        right_sum = 0
        ss = list(s)
        n = len(s)

        for i in reversed(range(n)):
            right_sum += shifts[i]

            diff = ord(ss[i]) - ord('a')
            diff = (diff + right_sum) % 26
            ss[i] = chr(diff + ord('a'))
        return "".join(ss)