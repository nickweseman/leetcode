class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            #print(f"complement {complement}")

            if complement in numMap:
                return [numMap[complement], i]
            else:
                numMap[num] = i

            #print(f"{numMap}")
        
        

        