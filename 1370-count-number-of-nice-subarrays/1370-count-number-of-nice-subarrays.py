class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(kk: int) -> int:
            odds = 0
            left = right = 0
            subarrays = 0

            while right < len(nums):
                if nums[right] % 2 == 1:
                    odds += 1
                while odds > kk:
                    if nums[left] % 2 == 1:
                        odds -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return helper(k) - helper(k - 1)