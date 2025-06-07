from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = right = 0
        window = defaultdict(int)
        longest = 0

        def window_invalid() -> bool:
            return len(s[left:right+1]) - max_freq > k

        def update_answer() -> None:
            nonlocal longest
            longest = max(longest, right - left + 1)

        while right < len(s):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            while window_invalid():
                print(f"{left=}")
                window[s[left]] -= 1
                left += 1
            update_answer()
            right += 1
        return longest