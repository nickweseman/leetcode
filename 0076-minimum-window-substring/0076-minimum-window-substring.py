from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)            # required character counts
        need   = len(target)           # distinct chars we must satisfy
        
        window = defaultdict(int)      # current window counts
        have   = 0                     # distinct chars satisfied
        
        left = 0
        right = 0
        n = len(s)
        
        best_len   = float('inf')
        best_start = 0

        def add(c):
            nonlocal have
            window[c] += 1
            if window[c] == target[c]:
                have += 1
        
        def remove(c):
            nonlocal have
            if window[c] == target[c]:
                have -= 1
            window[c] -= 1
        
        def update_answer(l, r):
            nonlocal best_len, best_start
            if r - l + 1 < best_len:
                best_len   = r - l + 1
                best_start = l
        
        while right < n:
            add(s[right])                       
            
            while left <= right and have == need:
                update_answer(left, right)      
                remove(s[left])                 
                left += 1
            
            right += 1
        
        return "" if best_len == float('inf') else s[best_start : best_start + best_len]
