class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        pairs = 0
        nums.sort()

        while left < right:
            print(f"{left=} {right=} {pairs=} {nums=}")
            if nums[left] + nums[right] < target:
                pairs += right - left
                left += 1
            else:
                right -= 1
        return pairs