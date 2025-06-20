class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        longest = 0

        while right < len(s):
            window[s[right]] += 1

            while len(window) < right - left + 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest