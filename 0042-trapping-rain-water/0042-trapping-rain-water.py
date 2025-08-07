class Solution:
    def trap(self, height: List[int]) -> int:
        # water[i] = min(max_left, max_right) * height[i]
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        rain = 0
        while left <= right:
            if max_left < max_right:
                if max_left - height[left] > 0:
                    print(left)
                    rain += max_left - height[left]
                max_left = max(max_left, height[left])
                left += 1
            else:
                if max_right - height[right] > 0:
                    print(right)
                    rain += max_right - height[right]
                max_right = max(max_right, height[right])
                right -= 1
        return rain