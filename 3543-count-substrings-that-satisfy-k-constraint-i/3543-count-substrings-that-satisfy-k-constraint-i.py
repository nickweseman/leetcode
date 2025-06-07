from collections import defaultdict
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        window = defaultdict(int)
        substrings = 0
        left = right = 0

        def window_invalid() -> None:
            return window['0'] > k and window['1'] > k

        def update_answer() -> None:
            nonlocal substrings
            substrings += right - left + 1

        while right < len(s):
            window[s[right]] += 1

            while window_invalid():
                window[s[left]] -= 1
                left += 1
            update_answer()
            right += 1
        return substrings