class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = []
        n = len(nums)
        counts = collections.Counter(nums)
        path = []
        def backtrack(index):
            if index == n:
                if len(path) > 0:
                    result.append(path.copy())
                return
            if nums[index] - k not in path and nums[index] + k not in path:
                if counts[nums[index]] > 0:
                    counts[nums[index]] -= 1
                    path.append(nums[index])
                    backtrack(index + 1)
                    path.pop()
                    counts[nums[index]] += 1
            backtrack(index + 1)
        backtrack(0)
        return len(result)
