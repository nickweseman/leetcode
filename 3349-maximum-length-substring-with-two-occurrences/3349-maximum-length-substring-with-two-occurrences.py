from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = right = 0
        max_length = float('-inf')
        window = defaultdict(int)

        while right < len(s):
            window[s[right]] += 1

            while left < right and window[s[right]] > 2:
                window[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

        