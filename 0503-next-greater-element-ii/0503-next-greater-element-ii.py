class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        result = [-1] * n

        for i in range(2 * n):
            actual_i = i % n
            num = nums[actual_i]

            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            if i < n:
                stack.append(i)
        return result