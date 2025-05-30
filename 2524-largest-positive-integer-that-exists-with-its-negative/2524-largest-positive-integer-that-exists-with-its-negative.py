class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right and nums[left] < 0 and nums[right] > 0:
            if abs(nums[left]) < abs(nums[right]):
                right -= 1
            elif abs(nums[left]) > abs(nums[right]):
                left += 1
            else:
                return nums[right]
        return -1
        