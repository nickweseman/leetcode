class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        result = []

        for i in range(1, n):
            candiesCount[i] += candiesCount[i - 1]
        
        for favorite_type, favorite_day, daily_cap in queries:
            min_eaten = favorite_day + 1
            max_eaten = (favorite_day + 1) * daily_cap

            if favorite_type == 0:
                first_favorite = 1
            else:
                first_favorite = candiesCount[favorite_type - 1] + 1
            last_favorite = candiesCount[favorite_type]

            can_reach = min_eaten <= last_favorite and max_eaten >= first_favorite
            result.append(can_reach)
        return result