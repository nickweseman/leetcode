class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = 0
        path = collections.Counter()
        def backtrack(index):
            nonlocal count
            if index == len(nums):
                if len(path) > 0:
                    count += 1
                return
            if path[nums[index] - k] == 0 and path[nums[index] + k] == 0:
                path[nums[index]] += 1
                backtrack(index + 1)
                path[nums[index]] -= 1
                if path[nums[index]] == 0:
                    del path[nums[index]]
            backtrack(index + 1)
        backtrack(0)
        return count