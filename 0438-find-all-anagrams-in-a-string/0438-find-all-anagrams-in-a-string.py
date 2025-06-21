class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target = collections.Counter(p)
        window = collections.Counter()
        left = right = 0

        have = 0
        need = len(target)

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                have += 1
            
            if right - left + 1 > len(p):
                if window[s[left]] == target[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1
            if right - left + 1 == len(p) and have == need:
                result.append(left)
            right += 1
        return result