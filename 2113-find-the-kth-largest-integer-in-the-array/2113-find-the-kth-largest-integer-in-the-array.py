class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        n = len(nums)
        k = n - k
        def quick_select(l, r):
            pivot_index = random.randint(l, r)
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]
        return str(quick_select(0, n - 1))
