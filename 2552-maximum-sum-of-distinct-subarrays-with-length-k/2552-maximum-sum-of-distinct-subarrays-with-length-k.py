class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = collections.defaultdict(int)
        left, right = 0, 0
        max_sum = sum = 0

        while right < len(nums):
            window[nums[right]] += 1
            sum += nums[right]

            if right - left + 1 > k:
                window[nums[left]] -= 1
                sum -= nums[left]
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            if right - left + 1 == k == len(window):
                max_sum = max(max_sum, sum)
            right += 1
        return max_sum