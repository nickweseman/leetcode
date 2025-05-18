class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowIndex = 1

        for fastIndex in range(1, len(nums)):
            if nums[slowIndex - 1] < nums[fastIndex]:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex
        