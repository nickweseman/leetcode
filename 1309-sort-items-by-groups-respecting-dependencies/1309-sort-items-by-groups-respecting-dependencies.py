class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        item_graph = collections.defaultdict(list)
        group_graph = collections.defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        num_groups = group_id
        for i in range(n):
            for before_item in beforeItems[i]:
                item_graph[i].append(before_item)
                if group[i] != group[before_item]:
                    group_graph[group[i]].append(group[before_item])
        def topo_sort(num_nodes, prereqs):
            cycle, visited = set(), set()
            output = []
            def dfs(node):
                if node in cycle:
                    return False
                if node in visited:
                    return True
                cycle.add(node)
                for pre in prereqs[node]:
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
        for item in sorted_items:
            group_map[group[item]].append(item)
        result = []
        for group_id in sorted_groups:
            result.extend(group_map[group_id])
        return result         