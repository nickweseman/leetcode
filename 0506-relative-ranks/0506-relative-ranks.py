class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = []
        for i, num in enumerate(score):
            max_heap.append((-num, i))
        heapq.heapify(max_heap)
        cur_place = 1
        result = [""] * len(score)
        while max_heap:
            index = heapq.heappop(max_heap)[1]
            match cur_place:
                case 1: result[index] = "Gold Medal"
                case 2: result[index] = "Silver Medal"
                case 3: result[index] = "Bronze Medal"
                case _: result[index] = str(cur_place)
            cur_place += 1
        return result 
