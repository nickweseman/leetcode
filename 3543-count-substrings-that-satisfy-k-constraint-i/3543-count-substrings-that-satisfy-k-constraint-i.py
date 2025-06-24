class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        substrings = 0

        while right < len(s):
            window[s[right]] += 1

            while window["0"] > k and window["1"] > k:
                window[s[left]] -= 1
                left += 1
            substrings += right - left + 1
            right += 1
        return substrings