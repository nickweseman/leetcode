class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result_set = set()
        n = len(nums)
        def backtrack(index):
            if index == n:
                return
            if not path or nums[index] >= path[-1]:
                path.append(nums[index])
                if len(path) >= 2:
                    result_set.add(tuple(path))
                backtrack(index + 1)
                path.pop()
            backtrack(index + 1)
        backtrack(0)
        return list(result_set)