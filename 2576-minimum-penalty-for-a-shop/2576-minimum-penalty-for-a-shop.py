class Solution:
    def bestClosingTime(self, customers: str) -> int:
        left_sum, right_sum = 0, customers.count("Y")
        min_penalty, min_index = right_sum, 0

        for i, state in enumerate(customers): 
            if state == "Y":
                right_sum -= 1
            else:
                left_sum += 1
            
            current_penalty = left_sum + right_sum
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                min_index = i + 1
        return min_index