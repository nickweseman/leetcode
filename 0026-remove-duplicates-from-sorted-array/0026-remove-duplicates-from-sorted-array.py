class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 1, 0
        while read < len(nums):
            if nums[read] != nums[write]:
                write += 1
                nums[read], nums[write] = nums[write], nums[read]
            read += 1
        return write + 1