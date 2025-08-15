class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        even_max_heap, odd_max_heap = [], []
        for i, val in enumerate(s):
            val = int(val)
            if val % 2 == 0:
                even_max_heap.append(-val)
            else:
                odd_max_heap.append(-val)
        heapq.heapify(even_max_heap)
        heapq.heapify(odd_max_heap)
        result = []
        for i, val in enumerate(s):
            val = int(val)
            if val % 2 == 0:
                result.append(str(-heapq.heappop(even_max_heap)))
            else:
                result.append(str(-heapq.heappop(odd_max_heap)))
        return int("".join(result))
