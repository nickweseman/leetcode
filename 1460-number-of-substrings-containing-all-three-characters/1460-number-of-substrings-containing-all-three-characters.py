from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def substringsAtMostK(k: int) -> int:
            window = defaultdict(int)
            left = right = 0
            subarrays = 0
            distinct = 0

            while right < len(s):
                window[s[right]] += 1
                if window[s[right]] == 1:
                    distinct += 1

                while left <= right and distinct > k:
                    if window[s[left]] == 1:
                        distinct -= 1
                    window[s[left]] -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return substringsAtMostK(3) - substringsAtMostK(2)
        