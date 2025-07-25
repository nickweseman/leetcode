class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        def backtrack(index):
            if index == n:
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()
            backtrack(index + 1)
        backtrack(0)
        return result