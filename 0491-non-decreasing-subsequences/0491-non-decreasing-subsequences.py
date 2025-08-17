class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        seen = set()
        def backtrack(index):
            if index == n:
                if len(path) >= 2:
                    t = tuple(path)
                    if t not in seen:
                        seen.add(t)
                        result.append(path.copy())
                return
            if not path or nums[index] >= path[-1]:
                path.append(nums[index])
                backtrack(index + 1)
                path.pop()
            backtrack(index + 1)
        backtrack(0)
        return result