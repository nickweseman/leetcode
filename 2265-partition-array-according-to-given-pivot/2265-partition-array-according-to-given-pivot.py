class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low, mid, high = [], [], []
        for num in nums:
            if num < pivot:
                low.append(num)
            elif num > pivot:
                high.append(num)
            else:
                mid.append(num)
        return low + mid + high