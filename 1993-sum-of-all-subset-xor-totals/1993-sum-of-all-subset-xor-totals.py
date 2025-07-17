class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(index, subtotal):
            nonlocal total
            if index == len(nums):
                total += subtotal
                return
            backtrack(index + 1, subtotal ^ nums[index])
            backtrack(index + 1, subtotal)
        backtrack(0, 0)
        return total