class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        vowels = set("aeiou")

        prefix_sum = [0]
        for word in words:
            is_vowel_string = (word[0] in vowels and word[-1] in vowels)
            prefix_sum.append(prefix_sum[-1] + is_vowel_string)
        
        for left, right in queries:
            ans.append(prefix_sum[right + 1] - prefix_sum[left])
        return ans