class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = set()
        def backtrack(index, remaining_sum):
            if index > 10:
                return
            if len(path) == k:
                if remaining_sum == 0:
                    result.append(list(path))
                return
            if remaining_sum < 0:
                return
            path.add(index)
            backtrack(index + 1, remaining_sum - index)
            path.remove(index)
            backtrack(index + 1, remaining_sum)
        backtrack(1, n)
        return result
