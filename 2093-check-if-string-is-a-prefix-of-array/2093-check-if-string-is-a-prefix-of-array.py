class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        need = scan = 0

        while need < len(words) and scan < len(s):
            word = words[need]
            if words[need] == s[scan:scan + len(word)]:
                need += 1
            else:
                return False
            scan += len(word)
            print(f"{scan=} {need=}")
        return scan == len(s)