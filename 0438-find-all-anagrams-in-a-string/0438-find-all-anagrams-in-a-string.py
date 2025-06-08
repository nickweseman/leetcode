from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter()
        target = Counter(p)
        
        left, right = 0, 0
        anagrams = []

        matches = 0
        required_matches = len(target)

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                matches += 1
            
            if right - left + 1 > len(p):
                if window[s[left]] == target[s[left]]:
                    matches -= 1
                window[s[left]] -= 1
                left += 1

            if right - left + 1 == len(p) and matches == required_matches:
                anagrams.append(left)
            right += 1
        return anagrams
        