class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total_substrings = (n * (n + 1)) // 2

        def atMost2() -> int:
            window = {'a':0, 'b':0, 'c':0}
            left = right = 0
            substrings = 0

            while right < len(s):
                window[s[right]] += 1

                while left <= right and window['a'] > 0 and window['b'] > 0 and window['c'] > 0:
                    window[s[left]] -= 1
                    left += 1
                substrings += right - left + 1
                right += 1
            return substrings
        return total_substrings - atMost2()