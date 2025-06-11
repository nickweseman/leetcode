class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        n = len(nums)
        total_subarrays = (n * (n+1)) // 2

        def atMost(kk: int) -> int:
            count = max_count = 0
            subarrays = 0
            left = right = 0

            while right < len(nums):
                if nums[right] == maxx:
                    count += 1

                while left <= right and count > kk:
                    if nums[left] == maxx:
                        count -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return total_subarrays - atMost(k - 1)
        