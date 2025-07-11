class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        k = n // 2
        def quick_select(l, r) -> int:
            p = l
            pivot_index = random.randint(l, r)
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]
        median = quick_select(0, n - 1)
        def map_index(i) -> int:
            return (2 * i + 1) % (n | 1)
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            map_mid = map_index(mid)
            if nums[map_mid] > median:
                map_low = map_index(low)
                nums[map_mid], nums[map_low] = nums[map_low], nums[map_mid]
                low += 1
                mid += 1
            elif nums[map_mid] == median:
                mid += 1
            else:
                map_high = map_index(high)
                nums[map_mid], nums[map_high] = nums[map_high], nums[map_mid]
                high -= 1 
        