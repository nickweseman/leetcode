class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numset = set(nums)
        nums.sort()

        for num in reversed(nums):
            if -num in numset:
                return num
        return -1
            