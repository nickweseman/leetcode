class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        path = []
        n = len(num)
        def backtrack(index, current_eval, last_operand):
            if index == n:
                if current_eval == target:
                    result.append("".join(path))
                return
            for i in range(index, n):
                # Abort entire branch if any number starts with zero and has more than one digit
                if i != index and num[index] == "0": 
                    break
                operand_str = num[index : i + 1]
                operand_int = int(operand_str)
                if index == 0: # no operator for the first number
                    path.append(operand_str)
                    backtrack(i + 1, operand_int, operand_int)
                    path.pop()
                else:
                    path.append("+" + operand_str)
                    backtrack(i + 1, current_eval + operand_int, operand_int)
                    path.pop()
                    path.append("-" + operand_str)
                    backtrack(i + 1, current_eval - operand_int, -operand_int) # last operand is NEGATIVE
                    path.pop()
                    path.append("*" + operand_str)
                    # undo the last operand and apply multiplication to it
                    new_eval = (current_eval - last_operand) + (last_operand * operand_int)
                    backtrack(i + 1, new_eval, last_operand * operand_int)
                    path.pop()
        backtrack(0, 0, 0)
        return result