class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        output = []

        while i < len(word1) and j < len(word2):
            output.append(word1[i])
            output.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            output.append(word1[i])
            i += 1
        while j < len(word2):
            output.append(word2[j])
            j += 1
        return "".join(output)
        