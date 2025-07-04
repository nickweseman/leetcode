class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        prefix_sums = list(itertools.accumulate(nums))
        
        for q in queries:
            left, right = 0, len(prefix_sums)
            while left < right:
                mid = (left + right) // 2
                if prefix_sums[mid] <= q:
                    left = mid + 1
                else:
                    right = mid
            answer.append(left)
        return answer