class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        substrings = 0

        while right < len(s):
            window[s[right]] += 1

            if right - left + 1 > 3:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if right - left + 1 == 3 == len(window):
                substrings += 1
            right += 1
        return substrings