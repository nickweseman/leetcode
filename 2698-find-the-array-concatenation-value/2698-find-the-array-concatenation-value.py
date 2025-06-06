class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_value = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            if left < right:
                concat_value += int(str(nums[left]) + str(nums[right]))
            else:
                concat_value += nums[left]
            left += 1
            right -= 1
        return concat_value