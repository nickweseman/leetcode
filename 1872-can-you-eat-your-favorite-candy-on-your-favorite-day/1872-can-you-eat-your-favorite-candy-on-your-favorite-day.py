class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        answer = []

        prefix_sum = [0]
        for count in candiesCount:
            prefix_sum.append(prefix_sum[-1] + count)
        
        for favorite_type, favorite_day, daily_cap in queries:
            min_eaten = favorite_day + 1
            max_eaten = (favorite_day + 1) * daily_cap

            first_favorite = prefix_sum[favorite_type] + 1
            last_favorite = prefix_sum[favorite_type + 1]

            can_reach = min_eaten <= last_favorite and max_eaten >= first_favorite
            answer.append(can_reach)
        return answer