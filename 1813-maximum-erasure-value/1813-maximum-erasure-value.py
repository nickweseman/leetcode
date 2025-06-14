class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = max_score = 0
        left = right = 0
        window = collections.defaultdict(int)

        while right < len(nums):
            window[nums[right]] += 1
            score += nums[right]

            while len(window) < right - left + 1:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                score -= nums[left]
                left += 1
            max_score = max(max_score, score)
            right += 1
        return max_score
                