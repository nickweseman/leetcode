class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        k_beauty = 0
        left = right = 0
        s = str(num)

        while right < len(s):
            if right - left + 1 > k:
                left += 1
            window = int(s[left:right+1])
            if right - left + 1 == k and window != 0 and num % window == 0:
                k_beauty += 1
            right += 1
        return k_beauty