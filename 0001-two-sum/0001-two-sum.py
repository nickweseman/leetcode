class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i, num in enumerate(nums):
            goal = target - num
            if goal in nummap:
                return [i, nummap[goal]]
            nummap[num] = i