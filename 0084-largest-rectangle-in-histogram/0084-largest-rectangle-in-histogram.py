class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # height, index
        max_area = 0
        for i, num in enumerate(heights):
            start = i
            while stack and stack[-1][0] > num:
                height, index = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((num, start))
        for height, index in stack:
            max_area = max(max_area, height * (len(heights) - index))
        return max_area