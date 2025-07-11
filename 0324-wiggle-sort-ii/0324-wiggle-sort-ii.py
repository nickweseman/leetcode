class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        def quick_select(l, r, k) -> int:
            pivot_index = random.randint(l, r)
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quick_select(l, p - 1, k)
            elif p < k:
                return quick_select(p + 1, r, k)
            else:
                return nums[p]
        # Find median
        median = quick_select(0, n - 1, n // 2)
        # Virtual indexing: maps 0->1, 1->3, 2->5, ..., n/2->0, n/2+1->2, n/2+2->4
        def map_index(i):
            return (2 * i + 1) % (n | 1)
        # 3-way partition using Dutch National Flag algorithm
        # low: > median, mid: = median, high: < median
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            mapped_mid = map_index(mid)
            if nums[mapped_mid] > median:
                mapped_low = map_index(low)
                nums[mapped_mid], nums[mapped_low] = nums[mapped_low], nums[mapped_mid]
                low += 1
                mid += 1
            elif nums[mapped_mid] < median:
                mapped_high = map_index(high)
                nums[mapped_mid], nums[mapped_high] = nums[mapped_high], nums[mapped_mid]
                high -= 1
            else:
                mid += 1