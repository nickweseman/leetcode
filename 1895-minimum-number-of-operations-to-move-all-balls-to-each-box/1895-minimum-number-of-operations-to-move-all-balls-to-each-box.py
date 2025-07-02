class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        left_balls = left_moves = 0
        for i in range(n):
            answer[i] += left_moves
            if boxes[i] == "1":
                left_balls += 1
            left_moves += left_balls
        
        right_balls = right_moves = 0
        for i in reversed(range(n)):
            answer[i] += right_moves
            if boxes[i] == "1":
                right_balls += 1
            right_moves += right_balls
        return answer