class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # index, height
        for i, val in enumerate(heights):
            start = i
            while stack and stack[-1][1] > val:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, val))
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        return max_area