class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target_sum = total // k
        n = len(nums)
        sums = [0] * k
        nums.sort(reverse=True)
        def backtrack(index):
            if index == n:
                return True
            for i in range(k):
                if sums[i] + nums[index] <= target_sum:
                    sums[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    sums[i] -= nums[index]
                    if sums[i] == 0:
                        break
            return False
        return backtrack(0)
