class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        read = write = 0

        while read < len(nums):
            if nums[read] % 2 == 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
            read += 1
        return nums