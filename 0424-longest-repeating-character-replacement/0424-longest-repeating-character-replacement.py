class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        longest = 0
        max_freq = 0

        while right < len(s):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            while left <= right and right - left + 1 - max_freq > k:
                window[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest