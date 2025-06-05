from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = right = 0
        window = defaultdict(int)
        max_length = float('-inf')

        while right < len(s):
            window[s[right]] += 1

            while any(True for freq in window.values() if freq > 2):
                window[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, (right - left + 1))
            right += 1
        return max_length
        