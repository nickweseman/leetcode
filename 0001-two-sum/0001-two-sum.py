class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i, num in enumerate(nums):
            nummap[num] = i
        for i, num in enumerate(nums):
            j = target - num
            if j in nummap:
                jnum = nummap[j]
                if i != jnum:
                    return [i, jnum]


