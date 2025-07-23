class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            max_heap.append((-a, 'a'))
        if b > 0:
            max_heap.append((-b, 'b'))
        if c > 0:
            max_heap.append((-c, 'c'))
        heapq.heapify(max_heap)
        result = []
        while max_heap:
            neg_freq1, ch1 = heapq.heappop(max_heap)
            freq1 = -neg_freq1
            freq1 -= 1
            if result[-2:] == [ch1, ch1]:
                if not max_heap:
                    break
                neg_freq2, ch2 = heapq.heappop(max_heap)
                freq2 = -neg_freq2
                freq2 -= 1
                result.append(ch2)
                if freq2 > 0:
                    heapq.heappush(max_heap, (-freq2, ch2))
            result.append(ch1)
            if freq1 > 0:
                heapq.heappush(max_heap, (-freq1, ch1))
        return "".join(result)