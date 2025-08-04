class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for num in nums:
            i = abs(num) - 1
            nums[i] = abs(nums[i]) * -1
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        return result