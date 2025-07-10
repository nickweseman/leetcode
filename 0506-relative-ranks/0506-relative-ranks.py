class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [""] * len(score)
        max_heap = []
        for i in range(len(score)):
            max_heap.append((-score[i], i))
        heapq.heapify(max_heap)
        current_rank = 1
        while max_heap:
            index = heapq.heappop(max_heap)[1]
            match current_rank:
                case 1: result[index] = "Gold Medal"
                case 2: result[index] = "Silver Medal"
                case 3: result[index] = "Bronze Medal"
                case _: result[index] = str(current_rank)
            current_rank += 1
        return result

        
