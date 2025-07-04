class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        prefix_sums = list(itertools.accumulate(nums))
        
        for q in queries:
            answer.append(bisect.bisect_right(prefix_sums, q))
        return answer