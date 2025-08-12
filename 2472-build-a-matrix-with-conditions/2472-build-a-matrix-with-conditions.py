class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(prereqs):
            cycle, visited = set(), set()
            output = []
            adj = collections.defaultdict(list)
            for pre, node in prereqs:
                adj[node].append(pre)
            def dfs(node):
                if node in cycle:
                    return False
                if node in visited:
                    return True
                cycle.add(node)
                for pre in adj[node]:
                    if not dfs(pre):
                        return False
                cycle.remove(node)
                visited.add(node)
                output.append(node)
                return True
            for i in range(1, k + 1):
                if not dfs(i):
                    return []
            return output
        sorted_rows = topo_sort(rowConditions)
        sorted_cols = topo_sort(colConditions)
        print(sorted_rows, sorted_cols)
        if not sorted_rows or not sorted_cols:
            return []
        row_val_to_i = {val:i for i, val in enumerate(sorted_rows)}
        col_val_to_i = {val:i for i, val in enumerate(sorted_cols)}
        result = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            r, c = row_val_to_i[i], col_val_to_i[i]
            result[r][c] = i
        return result
        


            
