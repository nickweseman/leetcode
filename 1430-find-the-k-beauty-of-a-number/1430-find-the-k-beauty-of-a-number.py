class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left = right = 0
        substrings = 0
        s = str(num)

        while right < len(s):
            if right - left + 1 > k:
                left += 1
            
            sub = int(s[left:right+1])
            if right - left + 1 == k and sub != 0 and num % sub == 0:
                substrings += 1
            right += 1
        return substrings
        