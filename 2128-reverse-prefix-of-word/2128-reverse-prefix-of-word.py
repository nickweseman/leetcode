class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w = list(word)
        idx = word.find(ch)

        if idx != -1:
            return word[:idx+1][::-1] + word[idx+1:]
        else:
            return word