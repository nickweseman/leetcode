class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        item_graph = []
        group_graph = []
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        num_groups = group_id
        for i in range(n):
            for before_item in beforeItems[i]:
                item_graph.append([i, before_item])
                if group[i] != group[before_item]:
                    group_graph.append([group[i], group[before_item]])
        def topo_sort(num_nodes, prereqs):
            cycle, visited = set(), set()
            output = []
            adj = collections.defaultdict(list)
            for node, pre in prereqs:
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
            for i in range(num_nodes):
                if not dfs(i):
                    return []
            return output
        sorted_items = topo_sort(n, item_graph)
        sorted_groups = topo_sort(num_groups, group_graph)
        if not sorted_items or not sorted_groups:
            return []
        group_map = collections.defaultdict(list)
        for i in range(n):
            item = sorted_items[i]
            group_map[group[item]].append(item)
        result = []
        for group_id in sorted_groups:
            result.extend(group_map[group_id])
        return result         