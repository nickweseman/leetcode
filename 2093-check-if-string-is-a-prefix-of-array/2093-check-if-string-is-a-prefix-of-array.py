class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        need = scan = 0

        while need < len(words) and scan < len(s):
            word = words[need]
            if s[scan:scan+len(word)] == word:
                need += 1
                scan += len(word)
            else:
                return False
        return scan == len(s)
        