class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left, right = 0, k - 1
        beauties = 0
        s = str(num)

        while right < len(s):
            while (right - left + 1) > k:
                left += 1

            div = int(s[left:right+1])
            if div != 0 and num % div == 0:
                beauties += 1
            
            right += 1
        return beauties
        