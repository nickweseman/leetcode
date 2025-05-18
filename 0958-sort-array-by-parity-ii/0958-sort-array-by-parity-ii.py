class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx = 0
        odd_idx = 1

        while even_idx < len(nums) and odd_idx < len(nums):
            if nums[even_idx] % 2 == 1 and nums[odd_idx] % 2 == 0:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            
            if nums[odd_idx] % 2 == 1:
                odd_idx += 2
        return nums