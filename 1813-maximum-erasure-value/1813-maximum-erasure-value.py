class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_total = 0
        total = 0
        left = right = 0
        distinct = 0
        window = collections.defaultdict(int)

        while right < len(nums):
            window[nums[right]] += 1
            if window[nums[right]] == 1:
                distinct += 1
            total += nums[right]
            
            while right - left + 1 > distinct:
                if window[nums[left]] == 1:
                    distinct -= 1
                window[nums[left]] -= 1
                total -= nums[left]
                left += 1
            max_total = max(max_total, total)
            right += 1
        return max_total