class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        answer = []

        prefix_sum = [0]
        for count in candiesCount:
            prefix_sum.append(prefix_sum[-1] + count)
        
        for favorite_type, favorite_day, daily_cap in queries:
            max_candies_eaten = (favorite_day + 1) * daily_cap
            first_favorite_candy = prefix_sum[favorite_type] + 1
            not_too_late = max_candies_eaten >= first_favorite_candy

            min_candies_eaten = favorite_day + 1
            last_favorite_candy = prefix_sum[favorite_type + 1]
            not_too_early = min_candies_eaten <= last_favorite_candy
            
            answer.append(not_too_late and not_too_early)
        return answer