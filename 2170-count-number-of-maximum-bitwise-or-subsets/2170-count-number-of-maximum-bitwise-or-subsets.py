class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        n = len(nums)
        count = 0
        def backtrack(index, or_so_far):
            nonlocal count
            if index == n:
                if or_so_far == max_or:
                    count += 1
                return
            backtrack(index + 1, or_so_far | nums[index])
            backtrack(index + 1, or_so_far)
        backtrack(0, 0)
        return count