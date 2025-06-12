class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        n = len(nums)

        for i in range(2 * n):
            actual_i = i % n
            num = nums[actual_i]

            while stack and nums[stack[-1]] < num:
                next_greater[stack.pop()] = num
            if i < n:
                stack.append(actual_i)
        return [next_greater.get(i, -1) for i in range(n)]