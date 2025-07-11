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
        median = quick_select(0, n - 1, n // 2)
        # Virtual index mapping - visits odd positions first, then even
        # i=0 → 1, i=1 → 3, i=2 → 5, ..., then wraps to evens
        def map_index(i):
            return (2 * i + 1) % (n | 1) # must be 2i + 1 because that prevents it from ever being n
            # if n = 6: n | 1 = 7, but if i = 3 (2 * 3) % 7 = 6 which is out of bounds!
        # 3-way partition using Dutch National Flag algorithm
        # Elements > median go to odd positions (visited first by our mapping)
        # Elements < median go to even positions (visited second by our mapping)
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            mapped_mid = map_index(mid)
            if nums[mapped_mid] > median:
                # Element belongs in odd position (which low is tracking)
                mapped_low = map_index(low)
                nums[mapped_mid], nums[mapped_low] = nums[mapped_low], nums[mapped_mid]
                low += 1
                mid += 1
            elif nums[mapped_mid] < median:
                # Element belongs in even position (which high is tracking)
                mapped_high = map_index(high)
                nums[mapped_mid], nums[mapped_high] = nums[mapped_high], nums[mapped_mid]
                high -= 1
            else:
                mid += 1