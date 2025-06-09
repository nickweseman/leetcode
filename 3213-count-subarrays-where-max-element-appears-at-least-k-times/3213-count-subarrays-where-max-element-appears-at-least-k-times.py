from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total_subarrays = (len(nums) * (len(nums) + 1)) // 2
        maxx = max(nums)
        
        def atMostK(kk: int) -> int:
            window = 0 # only need to track the number of times max occurs
            left = right = 0
            subarrays = 0

            while right < len(nums):
                if nums[right] == maxx:
                    window += 1

                while left <= right and window > kk:
                    if nums[left] == maxx:
                        window -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return total_subarrays - atMostK(k - 1)
        