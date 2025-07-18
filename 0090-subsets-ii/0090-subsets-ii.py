class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == nums[next_index - 1]:
                next_index += 1
            print(f"{index=}{next_index=}")
            backtrack(next_index)
        backtrack(0)
        return result