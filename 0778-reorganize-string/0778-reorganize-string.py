class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []
        counts = collections.Counter(s)
        n = len(s)
        for c, freq in counts.items():
            if freq > (n + 1) // 2:
                return ""
            max_heap.append((-freq, c))
        heapq.heapify(max_heap)
        result = []
        while max_heap:
            neg_freq1, c1 = heapq.heappop(max_heap)
            freq1 = -neg_freq1
            if result and result[-1] == c1:
                if not max_heap:
                    return ""
                neg_freq2, c2 = heapq.heappop(max_heap)
                freq2 = -neg_freq2
                result.append(c2)
                freq2 -= 1
                if freq2 > 0:
                    heapq.heappush(max_heap, (-freq2, c2))
            result.append(c1)
            freq1 -= 1
            if freq1 > 0:
                heapq.heappush(max_heap, (-freq1, c1))
        return "".join(result)