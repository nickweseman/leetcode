class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = math.inf
        kids = [0] * k
        def backtrack(index):
            nonlocal min_unfairness
            if index == len(cookies):
                min_unfairness = min(min_unfairness, max(kids))
                return
            for i in range(k):
                if kids[i] > min_unfairness:
                    break
                kids[i] += cookies[index]
                backtrack(index + 1)
                kids[i] -= cookies[index]
        backtrack(0)
        return min_unfairness