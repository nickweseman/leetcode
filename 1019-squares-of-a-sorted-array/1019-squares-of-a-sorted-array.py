class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        write = len(nums) - 1
        result = [0] * len(nums)

        while left <= right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2

            if left_squared < right_squared:
                result[write] = right_squared
                right -= 1
            else:
                result[write] = left_squared
                left += 1
            write -= 1
        return result
