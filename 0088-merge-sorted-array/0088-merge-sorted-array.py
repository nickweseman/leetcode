class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        ni = len(nums1) - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[ni] = nums2[j]
                j -= 1
            else:
                nums1[ni] = nums1[i]
                i -= 1
            ni -= 1
        
        if i < 0 and j >= 0:
            while ni >= 0:
                nums1[ni] = nums2[j]
                j -= 1
                ni -= 1
        if i >= 0 and j < 0:
            while ni >= 0:
                nums1[ni] = nums1[i]
                i -= 1
                ni -= 1

        