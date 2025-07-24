class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        all_vowels = set("aeiou")
        vowels = max_vowels = 0
        left = right = 0
        while right < len(s):
            if s[right] in all_vowels:
                vowels += 1
            if right - left + 1 > k:
                if s[left] in all_vowels:
                    vowels -= 1
                left += 1
            if right - left + 1 == k:
                max_vowels = max(max_vowels, vowels)
            right += 1
        return max_vowels