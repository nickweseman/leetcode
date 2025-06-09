class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        window = 0 # num vowels
        left = right = 0

        while right < len(s):
            if s[right] in vowels:
                window += 1

            while right - left + 1 > k:
                if s[left] in vowels:
                    window -= 1
                left += 1
            max_vowels = max(max_vowels, window)
            right += 1
        return max_vowels
        