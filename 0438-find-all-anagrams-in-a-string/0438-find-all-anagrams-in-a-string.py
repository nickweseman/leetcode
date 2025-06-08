from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter()
        target = Counter(p)
        
        left, right = 0, 0
        anagrams = []

        while right < len(s):
            window[s[right]] += 1
            
            if right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            if right - left + 1 == len(p) and target == window:
                anagrams.append(left)
            right += 1
        return anagrams
        