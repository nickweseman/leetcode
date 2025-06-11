class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(kk: int):
            window = collections.defaultdict(int)
            left = right = 0
            have = 0
            subarrays = 0
            
            while right < len(nums):
                window[nums[right]] += 1
                if window[nums[right]] == 1:
                    have += 1
                
                while have > kk:
                    if window[nums[left]] == 1:
                        have -= 1
                    window[nums[left]] -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return helper(k) - helper(k - 1)