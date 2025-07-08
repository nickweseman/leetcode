class Solution:
    def findMin(self, nums: List[int]) -> int:
        target = nums[-1]
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid
        return nums[left]