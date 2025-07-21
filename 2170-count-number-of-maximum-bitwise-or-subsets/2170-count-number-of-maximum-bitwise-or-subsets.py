class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        num_subsets = 0
        n = len(nums)
        def backtrack(index, or_so_far):
            nonlocal num_subsets, max_or
            if index == n:
                if or_so_far > max_or:
                    max_or = or_so_far
                    num_subsets = 1
                elif or_so_far == max_or:
                    num_subsets += 1
                return
            backtrack(index + 1, or_so_far | nums[index])
            backtrack(index + 1, or_so_far)
        backtrack(0, 0)
        return num_subsets
