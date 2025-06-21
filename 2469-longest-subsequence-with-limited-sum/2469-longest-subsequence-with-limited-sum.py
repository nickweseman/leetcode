class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = list(itertools.accumulate(nums))
        answer = []
        
        for q in queries:
            # `bisect_right` finds the insertion point for `q`, which is
            # equivalent to counting the number of prefix sums <= q.
            # This count is the maximum size of the subsequence.
            # Example: q=10, prefix_sums=[1,3,7,12]. bisect_right returns 3.
            size = bisect.bisect_right(prefix_sums, q)
            answer.append(size)
        return answer