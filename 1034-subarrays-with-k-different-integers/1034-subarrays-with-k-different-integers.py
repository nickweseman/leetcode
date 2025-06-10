class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(kk: int) -> int:
            window = collections.defaultdict(int)
            left = right = 0
            distinct = 0
            subarrays = 0

            while right < len(nums):
                window[nums[right]] += 1
                if window[nums[right]] == 1:
                    distinct += 1
                
                while left <= right and distinct > kk:
                    if window[nums[left]] == 1:
                        distinct -= 1
                    window[nums[left]] -= 1
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return atMost(k) - atMost(k-1)