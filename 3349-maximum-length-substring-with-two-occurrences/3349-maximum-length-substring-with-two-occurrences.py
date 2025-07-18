class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        max_length = -math.inf
        while right < len(s):
            window[s[right]] += 1
            while window[s[right]] > 2:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
