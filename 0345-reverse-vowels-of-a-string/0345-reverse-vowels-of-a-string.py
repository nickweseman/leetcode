class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        ss = list(s)

        while left < right:
            if ss[left] not in vowels:
                left += 1
            elif ss[right] not in vowels:
                right -= 1
            else:
                ss[left], ss[right] = ss[right], ss[left]
                left += 1
                right -= 1
        return "".join(ss)