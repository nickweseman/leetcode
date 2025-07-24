class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window = collections.defaultdict(int)
        left = right = 0
        n = len(s)
        total_subarrays = (n * (n + 1)) // 2
        subarrays = 0
        while right < n:
            window[s[right]] += 1
            while left <= right and window['a'] > 0 and window['b'] > 0 and window['c'] > 0:
                window[s[left]] -= 1
                left += 1
            subarrays += right - left + 1
            right += 1
        return total_subarrays - subarrays 