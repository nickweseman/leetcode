class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        n = len(nums)
        total_subarrays = (n * (n + 1)) // 2
        def atMostK(k_) -> int:
            left = right = 0
            count = 0
            subarrays = 0
            while right < len(nums):
                if nums[right] == maxx:
                    count += 1
                while count > k_:
                    if nums[left] == maxx:
                        count -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return total_subarrays - atMostK(k - 1)