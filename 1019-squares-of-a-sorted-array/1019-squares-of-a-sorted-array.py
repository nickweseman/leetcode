class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        result = [0] * len(nums)
        index = len(nums) - 1

        while left <= right:
            leftSquared = nums[left] ** 2
            rightSquared = nums[right] ** 2
            
            if leftSquared > rightSquared:
                result[index] = leftSquared
                left += 1
            else:
                result[index] = rightSquared
                right -= 1
            index -= 1
            
        return result

        