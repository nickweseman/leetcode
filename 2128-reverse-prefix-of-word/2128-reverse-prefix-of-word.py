class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w = list(word)
        idx = word.find(ch)

        if idx != -1:
            w = w[:idx+1][::-1] + w[idx+1:]
        return "".join(w)