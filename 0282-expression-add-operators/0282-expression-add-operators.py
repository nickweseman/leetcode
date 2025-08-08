class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        path = []
        result = []
        def backtrack(index, cur_val, last_operand):
            if index == n:
                if cur_val == target:
                    result.append("".join(path))
                return
            for i in range(index, n):
                operand_str = num[index : i + 1]
                operand = int(operand_str)
                if len(operand_str) > 1 and operand_str[0] == "0":
                    break
                if index == 0:
                    path.append(operand_str)
                    backtrack(i + 1, operand, operand)
                    path.pop()
                else:
                    path.append("+" + operand_str)
                    backtrack(i + 1, cur_val + operand, operand)
                    path.pop()
                    path.append("-" + operand_str)
                    backtrack(i + 1, cur_val - operand, -operand)
                    path.pop()
                    path.append("*" + operand_str)
                    new_val = (cur_val - last_operand) + (operand * last_operand)
                    backtrack(i + 1, new_val, (operand * last_operand))
                    path.pop()
        backtrack(0, 0, 0)
        return result