class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = set()
        n = len(nums)
        def backtrack(index):
            if index == n: 
                return
            for i in range(index, n):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    if len(path) >= 2:
                        result.add(tuple(path))
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)
        return list(result)