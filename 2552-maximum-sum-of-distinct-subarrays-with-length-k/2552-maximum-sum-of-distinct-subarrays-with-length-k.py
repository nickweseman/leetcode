class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = collections.defaultdict(int)
        total = max_total = 0
        left = right = 0
        while right < len(nums):
            window[nums[right]] += 1
            total += nums[right]
            if right - left + 1 > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                total -= nums[left]
                left += 1
            if right - left + 1 == k == len(window):
                max_total = max(max_total, total)
            right += 1
        return max_total