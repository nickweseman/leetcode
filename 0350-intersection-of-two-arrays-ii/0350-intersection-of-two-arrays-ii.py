class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = collections.Counter(nums1)
        n2 = collections.Counter(nums2)
        result = []

        for num1, freq in n1.items():
            if num1 in n2:
                result.extend([num1] * min(freq, n2[num1]))
        return result