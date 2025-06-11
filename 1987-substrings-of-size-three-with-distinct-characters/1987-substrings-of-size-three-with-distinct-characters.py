class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        substrings = 0
        distinct = 0

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == 1:
                distinct += 1

            if right - left + 1 > 3:
                if window[s[left]] == 1:
                    distinct -= 1
                window[s[left]] -= 1
                left += 1
            if right - left + 1 == 3 and distinct == 3:
                substrings += 1
            right += 1
        return substrings
            