class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allNums = set(range(len(nums) + 1))

        remainingNums = allNums - set(nums)
        
        return remainingNums.pop()
        