class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        path = collections.Counter()
        num_subsets = 0
        n = len(nums)
        def backtrack(index):
            nonlocal num_subsets
            if index == n:
                if len(path) > 0:
                    num_subsets += 1
                return
            if path[nums[index] - k] == 0 and path[nums[index] + k] == 0:
                path[nums[index]] += 1
                backtrack(index + 1)
                path[nums[index]] -= 1
                if path[nums[index]] == 0:
                    del path[nums[index]]
            backtrack(index + 1)
        backtrack(0)
        return num_subsets