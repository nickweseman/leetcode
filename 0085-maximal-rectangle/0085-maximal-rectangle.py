class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largest_histogram(heights):
            stack = [] # index, height
            max_area = 0
            for i, num in enumerate(heights):
                start = i
                while stack and stack[-1][1] > num:
                    index, height = stack.pop()
                    max_area = max(max_area, height * (i - index))
                    start = index
                stack.append((start, num))
            for index, height in stack:
                max_area = max(max_area, height * (len(heights) - index))
            return max_area
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * cols
        for r in range(rows):
            for c in range(cols):
                heights[c] = heights[c] + 1 if matrix[r][c] == "1" else 0
            max_area = max(max_area, largest_histogram(heights))
        return max_area