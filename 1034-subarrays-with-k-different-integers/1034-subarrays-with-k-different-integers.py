class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrays(k_):
            left = right = 0
            window = collections.defaultdict(int)
            subarrays = 0
            while right < len(nums):
                window[nums[right]] += 1
                while len(window) > k_:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                    left += 1
                subarrays += right - left + 1
                right += 1             
            return subarrays
        return subarrays(k) - subarrays(k - 1)