class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = max_score = 0
        window = collections.defaultdict(int)
        left = right = 0

        while right < len(nums):
            window[nums[right]] += 1
            score += nums[right]

            while right - left + 1 > len(window):
                window[nums[left]] -= 1
                score -= nums[left]
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            max_score = max(max_score, score)
            right += 1
        return max_score