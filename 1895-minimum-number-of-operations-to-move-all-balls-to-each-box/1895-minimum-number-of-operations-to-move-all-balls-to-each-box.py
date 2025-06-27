class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n 
        
        balls = moves = 0
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls
        
        balls = moves = 0
        for i in reversed(range(n)):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls
        
        return answer