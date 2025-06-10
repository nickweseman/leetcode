class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        left = right = 0
        num_vowels = 0
        max_vowels = 0

        while right < len(s):
            if s[right] in vowels:
                num_vowels += 1
            
            if right - left + 1 > k:
                if s[left] in vowels:
                    num_vowels -= 1
                left += 1
            if right - left + 1 == k:
                max_vowels = max(max_vowels, num_vowels)
            right += 1
        return max_vowels
        