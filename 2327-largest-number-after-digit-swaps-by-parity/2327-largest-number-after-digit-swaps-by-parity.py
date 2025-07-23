class Solution:
    def largestInteger(self, num: int) -> int:
        even_max_heap = []
        odd_max_heap = []
        s = str(num)
        n = len(s)
        for i in range(n):
            digit = int(s[i])
            if digit & 1 == 0:
                even_max_heap.append(-digit)
            else:
                odd_max_heap.append(-digit)
        heapq.heapify(even_max_heap)
        heapq.heapify(odd_max_heap)
        result = []
        for i in range(n):
            digit = int(s[i])
            if digit & 1 == 0:
                result.append(str(-heapq.heappop(even_max_heap)))
            else:
                result.append(str(-heapq.heappop(odd_max_heap)))
        return int("".join(result))
        
