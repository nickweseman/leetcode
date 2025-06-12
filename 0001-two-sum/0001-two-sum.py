class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            goal = target - num
            
            if goal in num_map:
                i2 = num_map[goal]
                if i != i2:
                    return [i, i2]
            num_map[num] = i