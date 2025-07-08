class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = collections.Counter()
        target = collections.Counter(t)
        have = 0
        need = len(target)
        left = right = 0
        min_window = ""
        min_length = math.inf

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                have += 1
            while left <= right and have == need:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]
                if window[s[left]] == target[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1
            right += 1
        return min_window