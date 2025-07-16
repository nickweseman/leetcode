class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        result = []
        for item, freq in counter.most_common(k):
            result.append(item)
        return result