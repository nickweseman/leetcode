class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] % 2 == 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1
        return nums