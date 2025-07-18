class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        path = []
        def backtrack(index):
            if index == len(nums):
                return
            if not path or nums[index] >= path[-1]:
                path.append(nums[index])
                if len(path) > 1:
                    result.add(tuple(path))
                backtrack(index + 1)
                path.pop()
            backtrack(index + 1)
        backtrack(0)
        return list(result)