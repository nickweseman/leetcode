class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    return mid
                left = mid + 1
            else:
                right = mid
        return -1