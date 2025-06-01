from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:           
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []
        for key in c1.keys() & c2.keys():
            result.extend([key] * min(c1[key], c2[key]))
        return result