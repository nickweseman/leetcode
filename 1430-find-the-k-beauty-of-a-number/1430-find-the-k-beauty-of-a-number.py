class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        left = right = 0
        substrings = 0

        while right < len(s):
            if right - left + 1 > k:
                left += 1
            val = int(s[left:right+1])
            if right - left + 1 == k and val != 0 and num % val == 0:
                substrings += 1
            right += 1
        return substrings