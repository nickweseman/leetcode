class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        comb = []
        n = len(nums)
        def dfs(i):
            if i == n:
                result.append(comb.copy())
                return
            comb.append(nums[i])
            dfs(i + 1)
            comb.pop()
            next_i = i + 1
            while next_i < n and nums[next_i] == nums[i]:
                next_i += 1
            dfs(next_i)
        dfs(0)
        return result