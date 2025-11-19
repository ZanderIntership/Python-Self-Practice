class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        moves = 0
        distance = 0
        for I in range(len(boxes)):
            # moves += 1
            for J in range(len(boxes)):
                if boxes[J] == "1":
                    # distance += 1
                    moves += abs(I - J)
            answer.append(moves)   
            moves = 0
        
        return answer
