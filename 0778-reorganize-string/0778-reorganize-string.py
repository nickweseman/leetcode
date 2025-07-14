class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        heap = []
        for c, freq in counts.items():
            if freq > math.ceil(len(s) / 2):
                return ""
            heap.append((-freq, c))
        heapq.heapify(heap)
        result = []
        prev_freq, prev_c = 0, ""
        for _ in range(len(s)):
            neg_freq, c = heapq.heappop(heap)
            freq = -neg_freq
            result.append(c)
            if prev_c:
                heapq.heappush(heap, (-prev_freq, prev_c))
            prev_c = c
            prev_freq = freq - 1
        return "".join(result)