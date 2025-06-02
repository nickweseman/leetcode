class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        output = list()
        while i < len(word1) and j < len(word2):
            output.append(word1[i])
            output.append(word2[j])
            i += 1
            j += 1
        output.extend(word1[i:])
        output.extend(word2[j:])
        return "".join(output)
        