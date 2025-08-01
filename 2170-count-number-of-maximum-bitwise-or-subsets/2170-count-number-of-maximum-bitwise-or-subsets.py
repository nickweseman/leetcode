class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        n = len(nums)
        num_or = 0
        def backtrack(index, or_sum):
            nonlocal num_or
            if index == n:
                if or_sum == max_or:
                    num_or += 1
                return
            backtrack(index + 1, or_sum | nums[index] )
            backtrack(index + 1, or_sum)
        backtrack(0, 0)
        return num_or