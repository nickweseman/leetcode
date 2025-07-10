class Solution:
    def kthLargestNumber(self, inums: List[str], k: int) -> str:
        inums = [int(x) for x in inums]
        k = len(inums) - k
        def quick_select(l, r) -> int:
            pivot_index = random.randint(l, r)
            inums[r], inums[pivot_index] = inums[pivot_index], inums[r]
            pivot = inums[r]
            p = l
            for i in range(l, r):
                if inums[i] <= pivot:
                    inums[i], inums[p] = inums[p], inums[i]
                    p += 1
            inums[p], inums[r] = inums[r], inums[p]
            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return inums[p]
        return str(quick_select(0, len(inums) - 1))