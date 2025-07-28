class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_total = 0
        n = len(nums)
        def backtrack(index, xor_so_far):
            nonlocal xor_total
            if index == n:
                xor_total += xor_so_far
                return
            backtrack(index + 1, xor_so_far ^ nums[index])
            backtrack(index + 1, xor_so_far)
        backtrack(0, 0)
        return xor_total

        