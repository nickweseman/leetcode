from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        left = right = 0
        longest = 0

        def window_invalid() -> bool:
            most_common_freq = window.most_common(1)[0][1]
            
            return (right - left + 1) - most_common_freq > k

        while right < len(s):
            window[s[right]] += 1

            while left <= right and window_invalid():
                window[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        return longest
        