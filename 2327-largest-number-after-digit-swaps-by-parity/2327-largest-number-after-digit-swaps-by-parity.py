class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        odd_max_heap = []
        even_max_heap = []
        for d in num_str:
            digit = int(d)
            if digit % 2 == 0:
                even_max_heap.append(-digit)
            else:
                odd_max_heap.append(-digit)
        heapq.heapify(even_max_heap)
        heapq.heapify(odd_max_heap)
        result = []
        for d in num_str:
            digit = int(d)
            if digit % 2 == 0:
                largest_even = -heapq.heappop(even_max_heap)
                result.append(str(largest_even))
            else:
                largest_odd = -heapq.heappop(odd_max_heap)
                result.append(str(largest_odd))
        return int("".join(result))