class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            actual_i = i % n
            while stack and nums[stack[-1]] < nums[actual_i]:
                result[stack.pop()] = nums[actual_i]
            if i < n:
                stack.append(i)
        return result