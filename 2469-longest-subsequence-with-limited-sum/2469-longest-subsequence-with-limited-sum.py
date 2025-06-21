class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = list(itertools.accumulate(nums))
        result = []

        for q in queries:
            size = bisect.bisect_right(prefix_sums, q)
            result.append(size)
        return result