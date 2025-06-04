class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left, right = 0, k - 1
        beauties = 0
        s = str(num)

        while right < len(s):
            div = int(s[left:right+1])
            print(f"{div=}")
            if div != 0 and num % div == 0:
                beauties += 1
            left += 1
            right += 1
        return beauties
        