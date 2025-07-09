class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = [(-score, i) for i, score in enumerate(score)]
        heapq.heapify(scores)
        result = [""] * len(scores)
        current_rank = 1
        while scores:
            index = heapq.heappop(scores)[1]
            match current_rank:
                case 1: result[index] = "Gold Medal"
                case 2: result[index] = "Silver Medal"
                case 3: result[index] = "Bronze Medal"
                case _: result[index] = str(current_rank)
            current_rank += 1
        return result

