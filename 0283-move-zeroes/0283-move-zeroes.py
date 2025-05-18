class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow_idx = 0

        for fast_idx in range(1, len(nums)):
            if nums[fast_idx] != 0 and nums[slow_idx] == 0:
                nums[slow_idx], nums[fast_idx] = nums[fast_idx], nums[slow_idx]

            if nums[slow_idx] != 0:
                    slow_idx += 1

            

        