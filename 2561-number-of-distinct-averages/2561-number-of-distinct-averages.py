class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs = set()
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            avgs.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return len(avgs)