class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        distinct = 0
        left = right = 0
        longest = 0

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == 1:
                distinct += 1
            while right - left + 1 > distinct:
                if window[s[left]] == 1:
                    distinct -= 1
                window[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
        
        