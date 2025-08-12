class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for item in range(n):
            if group[item] == -1:
                group[item] = group_id
                group_id += 1
        num_groups = group_id
        item_graph = collections.defaultdict(list)
        group_graph = collections.defaultdict(list)
        for item in range(n):
            for before in beforeItems[item]:
                item_graph[item].append(before)
                if group[item] != group[before]:
                    group_graph[group[item]].append(group[before])
        def topo_sort(num_nodes, prereqs):
            output = []
            cycle, visited = set(), set()
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
        group_items = collections.defaultdict(list)
        for item in sorted_items:
            group_items[group[item]].append(item)
        result = []
        for group in sorted_groups:
            result.extend(group_items[group])
        return result