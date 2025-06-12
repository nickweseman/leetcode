class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        max_score = float('-inf')
        left = right = 0
        window = collections.defaultdict(int)
        distinct = 0

        while right < len(nums):
            window[nums[right]] += 1
            if window[nums[right]] == 1:
                distinct += 1
            score += nums[right]
            
            while distinct < right - left + 1:
                if window[nums[left]] == 1:
                    distinct -= 1
                window[nums[left]] -= 1
                score -= nums[left]
                left += 1
            max_score = max(max_score, score)
            right += 1
        return max_score

        