class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = math.inf
        nums.sort()
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                test_sum = nums[i] + nums[left] + nums[right]
                if abs(test_sum - target) < abs(closest_sum - target):
                    closest_sum = test_sum
                if test_sum == target:
                    return test_sum
                if test_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum