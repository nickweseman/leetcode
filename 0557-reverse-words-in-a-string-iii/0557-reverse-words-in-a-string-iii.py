class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        output = []

        for word in words:
            output.append(word[::-1])
        return " ".join(output)
        
        