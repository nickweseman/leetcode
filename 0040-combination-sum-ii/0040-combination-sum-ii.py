class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start, combination, remaining_target):
            if remaining_target == 0:
                result.append(combination[:])
                return
            if remaining_target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(i + 1, combination, remaining_target - candidates[i])
                combination.pop()
        backtrack(0, [], target)
        return result
            

        backtrack(0, [], target)
        return result