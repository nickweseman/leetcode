class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid] == target:
                    return mid
                else:
                    right = mid
        #return left if left < len(nums) and nums[left] == target else -1
        return -1