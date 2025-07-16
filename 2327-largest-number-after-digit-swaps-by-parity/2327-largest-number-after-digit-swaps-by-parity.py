class Solution:
    def largestInteger(self, num: int) -> int:
        odd_max_heap = []
        even_max_heap = []
        s_num = str(num)
        for d in s_num:
            digit = int(d)
            if digit & 1:
                odd_max_heap.append(-digit)
            else:
                even_max_heap.append(-digit)
        heapq.heapify(odd_max_heap)
        heapq.heapify(even_max_heap)
        result = []
        for d in s_num:
            digit = int(d)
            if digit & 1:
                result.append(str(-heapq.heappop(odd_max_heap)))
            else:
                result.append(str(-heapq.heappop(even_max_heap)))
        return int("".join(result))