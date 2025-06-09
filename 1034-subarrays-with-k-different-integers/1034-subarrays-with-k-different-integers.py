from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtMost(kk: int) -> int:
            window = defaultdict(int)
            left = right = 0
            subarrays = 0

            while right < len(nums):
                window[nums[right]] += 1

                while len(window) > kk:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return  subarraysWithAtMost(k) - subarraysWithAtMost(k - 1)
        