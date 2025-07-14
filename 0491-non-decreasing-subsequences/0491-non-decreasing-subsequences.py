class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        comb = []
        def dfs(i):
            if i == len(nums):
                return
            if not comb or nums[i] >= comb[-1]:
                comb.append(nums[i])
                if len(comb) >= 2:
                    result_set.add(tuple(comb))
                dfs(i + 1)
                comb.pop()
            dfs(i + 1)
        dfs(0)
        return list(result_set)