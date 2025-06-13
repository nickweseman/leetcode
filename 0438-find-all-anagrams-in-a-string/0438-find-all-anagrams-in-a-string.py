class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target = collections.Counter(p)
        window = collections.Counter()

        left = right = 0

        while right < len(s):
            window[s[right]] += 1
            
            if right - left + 1 > len(p):
                window [s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if right - left + 1 == len(p) and target == window:
                result.append(left)
            right += 1
        return result
