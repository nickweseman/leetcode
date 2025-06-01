class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        scan = 0
        sentence_words = sentence.split(" ")

        while scan < len(sentence_words):
            if sentence_words[scan].startswith(searchWord):
                return scan + 1
            scan += 1
        return -1
        