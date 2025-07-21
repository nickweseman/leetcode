class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = sortedcontainers.SortedList()
        left = right = 0
        while right < len(nums):
            if right - left > indexDiff:
                window.remove(nums[left])
                left += 1
            pos = window.bisect_left(nums[right] - valueDiff)
            if pos < len(window) and window[pos] <= nums[right] + valueDiff:
                return True
            window.add(nums[right])
            right += 1
        return False