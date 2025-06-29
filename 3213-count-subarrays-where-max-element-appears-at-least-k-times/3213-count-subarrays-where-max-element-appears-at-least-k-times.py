class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        max_count = 0
        total_subarrays = (len(nums) * (len(nums) + 1)) // 2
        left = right = 0
        subarrays = 0

        while right < len(nums):
            if nums[right] == maxx:
                max_count += 1
            while left <= right and max_count > (k - 1):
                if nums[left] == maxx:
                    max_count -= 1
                left += 1
            subarrays += right - left + 1
            right += 1
        return total_subarrays - subarrays