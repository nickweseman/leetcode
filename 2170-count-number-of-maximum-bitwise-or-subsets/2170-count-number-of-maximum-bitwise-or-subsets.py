class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = -math.inf
        max_subsets = -1
        path = []
        def backtrack(index, or_so_far):
            nonlocal max_or, max_subsets
            if index == len(nums):
                if or_so_far > max_or:
                    max_or = or_so_far
                    max_subsets = 0 
                if or_so_far == max_or:
                    max_subsets += 1
                return
            backtrack(index + 1, or_so_far | nums[index])
            backtrack(index + 1, or_so_far)
        backtrack(0, 0)
        return max_subsets
            