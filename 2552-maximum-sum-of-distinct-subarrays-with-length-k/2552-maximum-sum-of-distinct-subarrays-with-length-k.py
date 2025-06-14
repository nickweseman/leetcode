class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        total = max_total = 0
        left = right = 0
        window = collections.defaultdict(int)

        while right < len(nums):
            total += nums[right]
            window[nums[right]] += 1

            if right - left + 1 > k:
                total -= nums[left]
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            if right - left + 1 == k == len(window):
                max_total = max(max_total, total)
            right +=1
        return max_total