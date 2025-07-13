class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor_sum = 0
        comb = []
        def dfs(i):
            nonlocal total_xor_sum
            if i == len(nums):
                local_xor = 0
                for c in comb:
                    local_xor ^= c
                total_xor_sum += local_xor
                return
            comb.append(nums[i])
            dfs(i + 1)
            comb.pop()
            dfs(i + 1)
        dfs(0)
        return total_xor_sum