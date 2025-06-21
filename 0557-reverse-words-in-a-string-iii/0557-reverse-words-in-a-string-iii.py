class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        result = []

        for i, word in enumerate(words):
            result.append("".join(reversed(word)))
        return " ".join(result)