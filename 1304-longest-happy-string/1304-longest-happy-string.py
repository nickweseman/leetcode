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
            neg_char1, c1 = heapq.heappop(max_heap)
            char1 = -neg_char1
            if result[-2:] == [c1, c1]:
                if not max_heap:
                    break
                neg_char2, c2 = heapq.heappop(max_heap)
                char2 = -neg_char2
                char2 -= 1
                result.append(c2)
                if char2 > 0:
                    heapq.heappush(max_heap, (-char2, c2))
            result.append(c1)
            char1 -= 1
            if char1 > 0:
                heapq.heappush(max_heap, (-char1, c1))   
        return "".join(result)