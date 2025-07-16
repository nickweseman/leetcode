class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def dfs(index):
            if index == len(nums):
                result.append(path.copy())
                return
            path.append(nums[index])
            dfs(index + 1)
            path.pop()
            dfs(index + 1)
        dfs(0)
        return result