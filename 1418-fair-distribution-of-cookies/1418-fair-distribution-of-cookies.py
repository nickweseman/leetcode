class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = math.inf
        kids = [0] * k
        def dfs(i):
            nonlocal min_unfairness
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(kids))
                return
            if max(kids) >= min_unfairness:
                return
            for kid_index in range(k):
                kids[kid_index] += cookies[i]
                dfs(i + 1)
                kids[kid_index] -= cookies[i]
                if kids[kid_index] == 0:
                    break
        dfs(0)
        return min_unfairness
        