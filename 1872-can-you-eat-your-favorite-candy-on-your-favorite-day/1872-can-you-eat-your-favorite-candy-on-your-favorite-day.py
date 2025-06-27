class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        answer = []

        for i in range(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]
        
        for favorite_type, favorite_day, daily_cap in queries:
            min_eaten = favorite_day + 1                # eat 1 per day
            max_eaten = (favorite_day + 1) * daily_cap  # eat daily_cap per day

            if favorite_type == 0:
                first_favorite = 1
            else:
                first_favorite = candiesCount[favorite_type - 1] + 1
            
            last_favorite = candiesCount[favorite_type]

            can_reach = max_eaten >= first_favorite and min_eaten <= last_favorite
            answer.append(can_reach)
        return answer