class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        kids = [0] * k
        n = len(cookies)
        min_unfairness = math.inf
        def backtrack(index):
            nonlocal min_unfairness
            if index == n:
                min_unfairness = min(min_unfairness, max(kids))
                return
            for i in range(k):
                kids[i] += cookies[index]
                backtrack(index + 1)
                kids[i] -= cookies[index]
                if kids[i] == 0:
                    break
        backtrack(0)
        return min_unfairness
        