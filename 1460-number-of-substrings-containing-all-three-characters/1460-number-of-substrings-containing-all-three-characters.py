class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = 0
        window = {'a': 0, 'b': 0, 'c': 0}
        substrings = 0
        
        while right < len(s):
            window[s[right]] += 1
            
            while window['a'] > 0 and window['b'] > 0 and window['c'] > 0:
                # Update answer BEFORE shrinking (current window is valid)
                # Key insight: If [left...right] contains all 3 chars,
                # then ALL substrings [0...left], [1...left], ..., [left...left]
                # extended to right are also valid
                window[s[left]] -= 1
                left += 1
            substrings += left
            right += 1
        return substrings
        