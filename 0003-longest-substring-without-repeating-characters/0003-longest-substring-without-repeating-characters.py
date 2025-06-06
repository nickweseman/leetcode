from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left = right = 0
        longest = 0

        while right < len(s):
            window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        return longest

        