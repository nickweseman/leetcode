from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = right = 0
        window = defaultdict(int)
        substrings = 0

        def is_valid() -> bool:
            nonlocal window
            for freq in window.values():
                if freq > 1:
                    return False
            return True

        while right < len(s):
            window[s[right]] += 1

            if right - left + 1 > 3:
                window[s[left]] -= 1
                left += 1
            
            if right - left + 1 == 3 and is_valid():
                substrings += 1
            right += 1
        return substrings