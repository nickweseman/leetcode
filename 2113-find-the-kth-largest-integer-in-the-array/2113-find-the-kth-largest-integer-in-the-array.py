class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        inums = [int(num) for num in nums]
        k = len(nums) - k
        def quick_select(l, r) -> int:
            p = l
            pivot_index = random.randint(l, r)
            inums[r], inums[pivot_index] = inums[pivot_index], inums[r]
            pivot = inums[r]
            for i in range(l, r):
                if inums[i] <= pivot:
                    inums[i], inums[p] = inums[p], inums[i]
                    p += 1
            inums[r], inums[p] = inums[p], inums[r]
            if p < k :
                return quick_select(p + 1, r)
            elif p > k:
                return quick_select(l, p - 1)
            else:
                return inums[p]
        return str(quick_select(0, len(inums) - 1))