class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        path = []
        result = []
        n = len(num)
        def backtrack(index, cur_eval, last_operand):
            if index == n:
                if cur_eval == target:
                    result.append("".join(path))
                return
            for i in range(index, n):
                operand_str = num[index : i + 1]
                operand_int = int(operand_str)
                if len(operand_str) > 1 and operand_str[0] == "0":
                    break
                if index == 0:
                    path.append(operand_str)
                    backtrack(i + 1, operand_int, operand_int)
                    path.pop()
                else:
                    path.append("+" + operand_str)
                    backtrack(i + 1, cur_eval + operand_int, operand_int)
                    path.pop()
                    path.append("-" + operand_str)
                    backtrack(i + 1, cur_eval - operand_int, -operand_int)
                    path.pop()
                    path.append("*" + operand_str)
                    new_eval = (cur_eval - last_operand) + (last_operand * operand_int)
                    backtrack(i + 1, new_eval, last_operand * operand_int)
                    path.pop()
        backtrack(0, 0, 0)
        return result