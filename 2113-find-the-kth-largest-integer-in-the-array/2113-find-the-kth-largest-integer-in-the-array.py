class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        k = n - k
        nums = [int(num) for num in nums]
        def quick_select(l, r):
            pivot_index = random.randint(l, r)
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                return quick_select(p + 1, r)
            elif p > k:
                return quick_select(l, p - 1)
            else:
                return nums[p]
        return str(quick_select(0, n - 1))