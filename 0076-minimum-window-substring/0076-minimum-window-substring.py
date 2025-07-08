class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = collections.Counter()
        target = collections.Counter(t)
        have = 0
        need = len(target)
        left = right = 0
        best_left, best_right = 0, math.inf

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                have += 1
            while left <= right and have == need:
                if right - left < best_right - best_left:
                    best_left, best_right = left, right
                if window[s[left]] == target[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1
            right += 1
        return "" if best_right == math.inf else s[best_left:best_right+1]