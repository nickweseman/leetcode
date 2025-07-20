class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target_sum = total // k
        buckets = [0] * k
        n = len(nums)
        nums.sort(reverse=True)
        def backtrack(index):
            if index == n:
                return True
            for i in range(k):
                if buckets[i] + nums[index] <= target_sum:
                    buckets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= nums[index]
                    if buckets[i] == 0:
                        break
            return False
        return backtrack(0)