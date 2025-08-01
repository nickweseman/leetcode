class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        result = set()
        def backtrack(index):
            if index == n:
                return
            for i in range(index, n):
                if path and path[-1] > nums[i]:
                    continue
                path.append(nums[i])
                if len(path) >= 2:
                    result.add(tuple(path))
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return list(result)