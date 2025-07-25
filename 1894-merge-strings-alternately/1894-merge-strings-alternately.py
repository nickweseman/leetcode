class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        merged = []
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            merged.append(word1[i])
            i += 1
        while j < len(word2):
            merged.append(word2[j])
            j += 1
        return "".join(merged)