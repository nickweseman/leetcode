from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = right = 0
        window = defaultdict(int)
        longest = 0

        while right < len(s):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            while right - left + 1 - max_freq > k:
                window[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest