class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        result = set()
        result.add(())
        def backtrack(index):
            if index == len(nums):
                return
            path.append(nums[index])
            result.add(tuple(path))
            backtrack(index + 1)
            path.pop()
            backtrack(index + 1)
        backtrack(0)
        return list(result)