class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = set()
        def backtrack(index):
            if index == len(nums):
                if len(path) > 1:
                    result.add(tuple(path))
                return
            if not path or not nums[index] < path[-1]:
                path.append(nums[index])
                backtrack(index + 1)
                path.pop()
            backtrack(index + 1)
        backtrack(0)
        return list(result)