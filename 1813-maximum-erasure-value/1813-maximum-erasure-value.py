from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = defaultdict(int)
        left = right = 0
        max_score = 0
        score = 0

        while right < len(nums):
            window[nums[right]] += 1
            score += nums[right]

            while len(window) < right - left + 1:
                window[nums[left]] -= 1
                score -= nums[left]
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            max_score = max(max_score, score)
            right += 1
        return max_score
        