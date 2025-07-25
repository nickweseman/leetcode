class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result_set = set()
        n = len(nums)
        def backtrack(index):
            if index == n:
                return
            num_used = set()
            for i in range(index, n):
                if nums[i] in num_used:
                    continue
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    num_used.add(nums[i])
                    if len(path) >= 2:
                        result_set.add(tuple(path))
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)
        return list(result_set)