class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        result = []

        prefix_sums = [0]
        for word in words:
            is_vowel_string = 1 if word[0] in vowels and word[-1] in vowels else 0
            prefix_sums.append(prefix_sums[-1] + is_vowel_string)
        
        for left, right in queries:
            result.append(prefix_sums[right + 1] - prefix_sums[left])
        return result
