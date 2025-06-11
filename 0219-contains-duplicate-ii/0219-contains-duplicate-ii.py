class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = collections.defaultdict(int)
        left = right = 0

        while right < len(nums):
            window[nums[right]] += 1

            while right - left > k:
                window[nums[left]] -= 1
                left += 1
            if window[nums[right]] > 1:
                return True
            right += 1
        return False