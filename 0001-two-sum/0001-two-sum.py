class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            goal = target - num
            if goal in num_map:
                return [i, num_map[goal]]
            num_map[num] = i
        