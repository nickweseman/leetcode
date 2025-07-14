class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        max_or_sum = 0
        for num in nums:
            max_or_sum |= num
        def dfs(i, current_or_sum):
            nonlocal count
            if i == len(nums):
                if current_or_sum == max_or_sum:
                    count += 1
                return
            dfs(i + 1, current_or_sum | nums[i])
            dfs(i + 1, current_or_sum)
        dfs(0, 0)
        return count