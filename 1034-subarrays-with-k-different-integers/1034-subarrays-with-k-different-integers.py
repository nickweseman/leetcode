class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(kk: int):
            subarrays = 0
            left = right = 0
            window = collections.defaultdict(int)

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
        return helper(k) - helper(k - 1)