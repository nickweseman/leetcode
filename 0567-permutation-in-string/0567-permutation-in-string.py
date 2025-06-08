from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter()
        target = Counter(s1)

        have = 0
        need = len(target)

        left, right = 0, 0

        while right < len(s2):
            window[s2[right]] += 1
            if window[s2[right]] == target[s2[right]]:
                have += 1
            
            while right - left + 1 > len(s1):
                if window[s2[left]] == target[s2[left]]:
                    have -= 1
                window[s2[left]] -= 1
                left += 1
            
            if have == need:
                return True
            right += 1
        return False
        