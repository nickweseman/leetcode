class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        need = scan = 0
        while scan < len(s) and need < len(words):
            word = words[need]
            if s[scan:scan+len(word)] == word:
                need += 1
            else:
                return False
            scan += len(word)
        return scan == len(s)