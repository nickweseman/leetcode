class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        buckets = [0] * k
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = sum(nums) // k
        n = len(nums)
        def backtrack(index):
            if index == n:
                return True
            for i in range(k):
                num = nums[index]
                if num + buckets[i] <= target_sum:
                    buckets[i] += num
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= num
                #optimization: if you tried putting in an empty bucket and it failed, no point in doing the same with the rest of the empty buckets
                    if buckets[i] == 0: 
                        break
            return False
        return backtrack(0)