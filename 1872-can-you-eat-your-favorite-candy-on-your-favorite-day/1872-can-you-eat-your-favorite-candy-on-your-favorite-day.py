class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        answer = []

        for i in range(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]
        
        for favorite_type, favorite_day, daily_cap in queries:
            max_eaten = (favorite_day + 1) * daily_cap  # eat daily_cap per day
            min_eaten = favorite_day + 1                # eat 1 per day

            if favorite_type == 0:
                first_favorite = 1
            else:
                first_favorite = candiesCount[favorite_type - 1] + 1
            last_favorite = candiesCount[favorite_type]  # this represents the prefix sum for the next favorite type, can't be bigger than this 

            not_too_late = max_eaten >= first_favorite
            not_too_early = min_eaten <= last_favorite
            
            answer.append(not_too_late and not_too_early)
        return answer