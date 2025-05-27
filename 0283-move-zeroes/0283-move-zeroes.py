class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

            

        