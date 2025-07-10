class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        for c, freq in counter.items():
            if freq > (len(s) + 1) // 2:
                return ""
        max_heap = [(-freq, c) for c, freq in counter.items()]
        heapq.heapify(max_heap)
        prev_freq, prev_c = -1, ""
        result = []
        while max_heap:
            neg_freq, c = heapq.heappop(max_heap)
            freq = -neg_freq
            result.append(c)
            if prev_freq > 0:
                heapq.heappush(max_heap, (-prev_freq, prev_c))
            prev_freq = freq - 1
            prev_c = c
        return "".join(result)
                