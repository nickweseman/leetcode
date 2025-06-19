class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = collections.Counter()
        target = collections.Counter(t)

        left = right = 0

        have = 0
        need = len(target)

        best_left, best_right = 0, float('inf')

        def add():
            nonlocal have
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                have += 1
        def remove():
            nonlocal have
            if window[s[left]] == target[s[left]]:
                have -= 1
            window[s[left]] -= 1
        def windowValid():
            return have == need
        def updateAnswer(l: int, r: int):
            nonlocal best_left, best_right
            if r - l < best_right - best_left:
                best_left, best_right = l, r

        while right < len(s):
            add()

            while left <= right and windowValid():
                updateAnswer(left, right)
                remove()
                left += 1
            right += 1
        print(locals())
        return "" if best_right == float('inf') else s[best_left: best_right + 1]