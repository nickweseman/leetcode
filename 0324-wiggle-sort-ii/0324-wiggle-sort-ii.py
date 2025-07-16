class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        k = n // 2
        def get_median(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p < k:
                return get_median(p + 1, r)
            elif p > k:
                return get_median(l, p - 1)
            else:
                return nums[p]
        median = get_median(0, n - 1)
        def map_index(i):
            return (2 * i + 1) % (n | 1)
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            mapped_mid = map_index(mid)
            if nums[mapped_mid] > median:
                mapped_low = map_index(low)
                nums[mapped_low], nums[mapped_mid] = nums[mapped_mid], nums[mapped_low]
                low += 1
                mid += 1
            elif nums[mapped_mid] < median:
                mapped_high = map_index(high)
                nums[mapped_high], nums[mapped_mid] = nums[mapped_mid], nums[mapped_high]
                high -= 1
            else:
                mid += 1
                
        