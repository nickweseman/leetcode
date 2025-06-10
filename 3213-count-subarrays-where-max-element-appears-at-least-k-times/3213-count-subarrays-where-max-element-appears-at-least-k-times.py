class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_subarrays = (n * (n + 1)) // 2

        def helper() -> int:
            maxx = max(nums)
            max_count = 0
            left = right = 0
            subarrays = 0

            while right < len(nums):
                if nums[right] == maxx:
                    max_count += 1
                
                while max_count > k - 1:
                    if nums[left] == maxx:
                        max_count -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return total_subarrays - helper()