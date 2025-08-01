class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        visited.add("0000")
        queue = collections.deque()
        queue.append(("0000", 0))
        def get_children(lock):
            result = []
            for i in range(4):
                digit = int(lock[i])
                fwd_digit = digit + 1 if digit < 9 else 0
                bwd_digit = digit - 1 if digit > 0 else 9
                result.append(lock[:i] + str(fwd_digit) + lock[i + 1:])
                result.append(lock[:i] + str(bwd_digit) + lock[i + 1:])
            return result
        while queue:
            for _ in range(len(queue)):
                lock, turns = queue.popleft()
                if lock == target:
                    return turns
                for child in get_children(lock):
                    if child not in visited:
                        visited.add(child)
                        queue.append((child, turns + 1))
        return -1