class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        for count in counts.values():
            if count > (len(s) + 1) // 2:
                return ""
        heap = [(-freq, c) for c, freq in counts.items()]
        heapq.heapify(heap)
        result = []
        prev_count, prev_c = 0, ""

        while heap:
            skip_first = False
            if result and heap[0][1] == result[-1]:
                topfreq, topc  = heapq.heappop(heap)
                topfreq = -topfreq
                skip_first = True
            freq, c = heapq.heappop(heap)
            freq = -freq
            result.append(c)
            freq -= 1
            if freq > 0:
                heapq.heappush(heap, (-freq, c))
            if skip_first:
                heapq.heappush(heap, (-topfreq, topc))
        return "".join(result)
            