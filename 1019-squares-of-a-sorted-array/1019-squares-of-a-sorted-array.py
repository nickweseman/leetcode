class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        write = right

        while left <= right and write >= 0:
            left_squared = nums[left] * nums[left]
            right_squared = nums[right] * nums[right]
            if left_squared < right_squared:
                result[write] = right_squared
                right -= 1
            else:
                result[write] = left_squared
                left += 1
            write -= 1
        return result