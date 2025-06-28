class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        window = collections.defaultdict(int)
        left = right = 0
        have = 0
        need = len(target)

        while right < len(s2):
            window[s2[right]] += 1
            if window[s2[right]] == target[s2[right]]:
                have += 1
            if right - left + 1 > len(s1):
                if window[s2[left]] == target[s2[left]]:
                    have -= 1
                window[s2[left]] -= 1
                left += 1
            if right - left + 1 == len(s1) and have == need:
                return True
            right += 1
        return False