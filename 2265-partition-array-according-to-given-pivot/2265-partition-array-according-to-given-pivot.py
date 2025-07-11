class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low, med, high = [], [], []
        for num in nums:
            if num < pivot:
                low.append(num)
            elif num == pivot:
                med.append(num)
            else:
                high.append(num)
        return low + med + high