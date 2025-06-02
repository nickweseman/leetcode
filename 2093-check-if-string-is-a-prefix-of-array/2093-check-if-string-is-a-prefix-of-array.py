class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        need = scan = 0

        while need < len(s) and scan < len(words):
            word = words[scan]
            if s[need:need+len(word)] == word:
                need += len(word)
            else:
                return False
            scan += 1
        return need == len(s)