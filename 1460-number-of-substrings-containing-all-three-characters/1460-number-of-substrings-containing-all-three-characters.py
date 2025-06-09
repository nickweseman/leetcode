from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def substringsAtMostK(k: int) -> int:
            window = defaultdict(int)
            left = right = 0
            subarrays = 0

            def distinctK() -> bool:
                total = 0
                for freq in window.values():
                    if freq > 0:
                        total += 1
                return total

            while right < len(s):
                window[s[right]] += 1

                while left <= right and distinctK() > k:
                    window[s[left]] -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return substringsAtMostK(3) - substringsAtMostK(2)
        