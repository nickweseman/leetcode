from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total_subarrays = (len(nums) * (len(nums) + 1)) // 2
        maxx = max(nums)
        
        def atMostK(kk: int) -> int:
            window = defaultdict(int)
            left = right = 0
            subarrays = 0

            while right < len(nums):
                window[nums[right]] += 1

                while left <= right and window[maxx] > kk:
                    window[nums[left]] -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return total_subarrays - atMostK(k - 1)
        