class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = math.inf
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if abs(sum_ - target) < abs(closest_sum - target):
                    closest_sum = sum_
                if sum_ == target:
                    return sum_
                elif sum_ < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
