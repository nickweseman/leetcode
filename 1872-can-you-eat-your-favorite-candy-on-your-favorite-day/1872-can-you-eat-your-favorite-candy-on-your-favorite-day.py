class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_sum = [0]
        for num in candiesCount:
            prefix_sum.append(prefix_sum[-1] + num)
        result = []
        for favorite_type, favorite_day, daily_cap in queries:
            min_eaten = favorite_day + 1
            max_eaten = daily_cap * (favorite_day + 1)
            first_favorite = prefix_sum[favorite_type] + 1
            last_favorite = prefix_sum[favorite_type + 1]
            can_reach = min_eaten <= last_favorite and max_eaten >= first_favorite
            result.append(can_reach)
        return result