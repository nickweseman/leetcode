class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write, read = 1, 1

        while read < len(nums):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write