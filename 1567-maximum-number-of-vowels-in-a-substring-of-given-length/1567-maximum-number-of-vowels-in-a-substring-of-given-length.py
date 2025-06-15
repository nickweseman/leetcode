class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        vowel_count = max_vowels = 0
        left = right = 0

        while right < len(s):
            if s[right] in vowels:
                vowel_count += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
            if right - left + 1 == k:
                max_vowels = max(max_vowels, vowel_count)
            right += 1
        return max_vowels
