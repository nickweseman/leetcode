class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        total_subarrays = (len(nums) * (len(nums) + 1)) // 2
        subarrays = 0
        left = right = 0
        max_count = 0

        while right < len(nums):
            if nums[right] == maxx:
                max_count += 1
            while max_count >= k:
                if nums[left] == maxx:
                    max_count -= 1
                left += 1
            subarrays += right - left + 1
            right += 1
        return total_subarrays - subarrays