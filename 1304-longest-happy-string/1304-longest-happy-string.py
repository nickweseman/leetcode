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
            ch = max_heap[0][1]
            if result[-2:] == [ch, ch]:
                print("got here")
                neg_count1, letter1 = heapq.heappop(max_heap)
                count1 = -neg_count1
                if not max_heap:
                    break
                neg_count2, letter2 = heapq.heappop(max_heap)
                count2 = -neg_count2
                count2 -= 1
                result.append(letter2)
                if count2 > 0:
                    heapq.heappush(max_heap, (-count2, letter2))
                heapq.heappush(max_heap, (-count1, letter1))
            else:
                neg_count, letter = heapq.heappop(max_heap)
                count = -neg_count
                count -= 1
                result.append(letter)
                if count > 0:
                    heapq.heappush(max_heap, (-count, letter))
        return "".join(result)