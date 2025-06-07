from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(target)

        left = right = 0
        best_left, best_right = 0, float('inf')

        def add(c: str) -> None:
            nonlocal have
            window[c] += 1
            if target[c] == window[c]:
                have += 1
        
        def remove(c: str) -> None:
            nonlocal have
            if target[c] == window[c]:
                have -= 1
            window[c] -= 1
        
        def window_valid() -> bool:
            return left <= right and have == need
        
        def update_answer() -> None:
            nonlocal best_left, best_right
            if right - left < best_right - best_left:
                best_left, best_right = left, right
        
        while right < len(s):
            add(s[right])
            while window_valid():
                update_answer()
                remove(s[left])
                left += 1
            right += 1
        return "" if best_right == float('inf') else s[best_left: best_right + 1]
        