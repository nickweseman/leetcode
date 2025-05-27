class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1

        for fast in range(1, len(nums)):
            if nums[slow - 1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
        