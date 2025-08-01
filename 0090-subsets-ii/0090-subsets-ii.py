class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        result = []
        n = len(nums)
        def backtrack(index):
            if index == n:
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index + 1)
            while index  + 1 < n and nums[index] == nums[index + 1]:
                index += 1
            path.pop()
            backtrack(index + 1)
        backtrack(0)
        return result
