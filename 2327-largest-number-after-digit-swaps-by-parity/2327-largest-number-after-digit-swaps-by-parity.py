class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        odd_max_heap = []
        even_max_heap = []
        for d in s:
            digit = int(d)
            if digit & 1 == 1:
                odd_max_heap.append(-digit)
            else:
                even_max_heap.append(-digit)
        heapq.heapify(odd_max_heap)
        heapq.heapify(even_max_heap)
        result = []
        for d in s:
            digit = int(d)
            if digit & 1 == 1:
                result.append(str(-heapq.heappop(odd_max_heap)))
            else:
                result.append(str(-heapq.heappop(even_max_heap)))
        return int("".join(result))
            

