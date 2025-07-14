class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        heap = []
        for c, freq in counts.items():
            if freq > (len(s) + 1) // 2:
                return ""
            heap.append((-freq, c))
        heapq.heapify(heap)
        result = []
        prev_freq, prev_c = 0, ""
        while heap:
            neg_freq, c = heapq.heappop(heap)
            freq = -neg_freq
            result.append(c)
            if prev_c and prev_freq > 0:
                heapq.heappush(heap, (-prev_freq, prev_c))
            prev_c = c
            prev_freq = freq - 1
        return "".join(result)