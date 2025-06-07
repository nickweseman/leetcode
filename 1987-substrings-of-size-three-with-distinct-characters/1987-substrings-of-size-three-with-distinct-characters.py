from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window = defaultdict(int)
        left = right = 0
        substrings = 0

        def window_valid() -> bool:
            return all(freq < 2 for freq in window.values())

        while right < len(s):
            window[s[right]] += 1

            if right - left + 1 > 3:
                window[s[left]] -= 1
                left += 1
            if right - left + 1 == 3 and window_valid():
                substrings += 1
            right += 1
        return substrings
        