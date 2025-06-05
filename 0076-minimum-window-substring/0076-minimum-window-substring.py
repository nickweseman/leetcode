from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        target = Counter(t)

        left = right = 0
        best_left, best_right = 0, -1

        have = 0
        need = len(target)

        def add(c: str):
            nonlocal have
            window[c] += 1
            if window[c] == target[c]:
                have += 1
    
        def remove(c: str):
            nonlocal have
            if window[c] == target[c]:
                have -= 1
            window[c] -= 1
        
        def update_answer(l: int, r: int):
            nonlocal best_left, best_right
            if r - l < best_right - best_left or best_right == -1:
                best_left, best_right = l, r
        
        while right < len(s):
            add(s[right])

            while left <= right and have == need:
                update_answer(left, right)
                remove(s[left])
                left += 1
            right += 1
        print(f"{best_right}")
        return "" if best_right == -1 else s[best_left: best_right + 1]