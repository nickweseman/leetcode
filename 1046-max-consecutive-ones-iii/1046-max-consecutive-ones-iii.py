from collections import defaultdict
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = 0
        left = right = 0
        maximum = 0

        while right < len(nums):
            if nums[right] == 0:
                window += 1

            while window > k:
                if nums[left] == 0:
                    window -= 1
                left += 1
            maximum = max(maximum, right - left + 1)
            print(f"{left=} {right=}")
            right += 1
        return maximum
