class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        shuffle(nums)
        
        def part(lo, hi): 
            """Return partition of nums[lo:hi]."""
            i, j = lo+1, hi-1
            while i <= j: 
                if nums[i] < nums[lo]: i += 1
                elif nums[lo] < nums[j]: j -= 1
                else: 
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[lo], nums[j] = nums[j], nums[lo]
            return j 
        
        lo, hi = 0, len(nums)
        while lo < hi: 
            mid = part(lo, hi)
            if mid == len(nums)-k: return str(nums[mid])
            elif mid < len(nums)-k: lo = mid + 1
            else: hi = mid
        