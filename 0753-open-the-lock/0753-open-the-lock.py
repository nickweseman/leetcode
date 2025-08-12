class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = set(deadends) | set("0000")
        queue = collections.deque([("0000", 0)]) # lock, turns
        def get_children(lock):
            children = []
            for i in range(4):
                digit = int(lock[i])
                fwd_digit = digit + 1 if digit < 9 else 0
                bwd_digit = digit - 1 if digit > 0 else 9
                children.append(lock[:i] + str(fwd_digit) + lock[i+1:])
                children.append(lock[:i] + str(bwd_digit) + lock[i+1:])
            return children
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for child in get_children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))
        return -1
        