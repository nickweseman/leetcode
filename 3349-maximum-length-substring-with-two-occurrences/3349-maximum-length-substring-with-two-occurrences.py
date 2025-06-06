from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = right = 0
        max_length = float('-inf')
        window = defaultdict(int)

        def window_valid() -> bool:
            nonlocal window
            for freq in window.values():
                if freq > 2:
                    return False
            return True

        while right < len(s):
            window[s[right]] += 1

            while left < right and not window_valid():
                window[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

        