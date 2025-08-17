class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            num = abs(num)
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
            else:
                result.append(num)
        return result