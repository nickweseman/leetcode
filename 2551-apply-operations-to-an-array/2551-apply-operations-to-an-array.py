class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        slow_idx = 0

        for fast_idx in range(1, len(nums)):
            if nums[slow_idx] == 0 and nums[fast_idx] != 0:
                nums[slow_idx], nums[fast_idx] = nums[fast_idx], nums[slow_idx]
            if nums[slow_idx] != 0:
                slow_idx += 1
        return nums

        