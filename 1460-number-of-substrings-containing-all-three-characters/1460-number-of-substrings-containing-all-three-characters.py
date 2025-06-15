class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total_substrings = (len(s) * (len(s) + 1)) // 2
        substrings = 0
        left = right = 0
        window = {"a":0, "b":0, "c":0}

        while right < len(s):
            window[s[right]] += 1

            while window["a"] > 0 and window["b"] > 0 and window["c"] > 0:
                window[s[left]] -= 1
                left += 1
            substrings += right - left + 1
            right += 1
        return total_substrings - substrings