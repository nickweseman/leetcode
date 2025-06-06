from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(target)

        left, right = 0, 0
        best_left, best_right = 0, float('inf')

        def add(c: str) -> None:
            nonlocal have
            window[c] += 1
            if window[c] == target[c]:
                have += 1
        
        def remove(c: str) -> None:
            nonlocal have
            if window[c] == target[c]:
                have -= 1
            window[c] -= 1

        def window_valid() -> bool:
            nonlocal have, need
            return have == need
        
        def update_answer(l: int, r: int) -> None:
            nonlocal best_left, best_right
            if r - l < best_right - best_left:
                best_left, best_right = l, r
        
        while right < len(s):
            add(s[right])

            while left <= right and window_valid():
                update_answer(left, right)
                remove(s[left])
                left += 1
            right += 1
        return "" if best_right == float('inf') else s[best_left: best_right + 1]
        