from collections import defaultdict

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = right = 0
        window = defaultdict(int)
        substrings = 0

        while right < len(s):
            window[s[right]] += 1

            while window[s[right]] > 1 or right - left + 1 > 3:
               window[s[left]] -= 1
               left += 1

            if right - left + 1 == 3:
                substrings += 1

            right += 1
        return substrings
        