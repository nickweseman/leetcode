class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq = 0
        left = right = 0
        longest = 0
        window = collections.defaultdict(int)

        while right < len(s):
            window[s[right]] += 1
            most_freq = max(most_freq, window[s[right]])

            while right - left + 1 - most_freq > k:
                window[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest