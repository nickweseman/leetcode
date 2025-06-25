class Solution:
    def bestClosingTime(self, customers: str) -> int:
        left_sum, right_sum = 0, customers.count("Y")
        min_penalty = math.inf
        min_index = -1

        for i, num in enumerate(customers):
            curr_penalty = left_sum + right_sum
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                min_index = i
            
            if num == "Y":
                right_sum -= 1
            else:
                left_sum += 1
        curr_penalty = left_sum + right_sum
        if curr_penalty < min_penalty:
            min_penalty = curr_penalty
            min_index = len(customers)
        return min_index
