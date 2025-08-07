class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        num_groups = group_id
        item_graph = collections.defaultdict(list)
        group_graph = collections.defaultdict(list)
        for item in range(n):
            for prereq in beforeItems[item]:
                item_graph[item].append(prereq)
                if group[prereq] != group[item]:
                    group_graph[group[item]].append(group[prereq])
        def topo_sort(num_nodes, prereq_map):
            visited, cycle = set(), set()
            output = []
            def dfs(node):
                if node in cycle:
                    return False
                if node in visited:
                    return True
                cycle.add(node)
                for prereq in prereq_map[node]:
                    if not dfs(prereq):
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
        group_to_items = collections.defaultdict(list)
        for item in sorted_items:
            group_to_items[group[item]].append(item)
        result = []
        for group_id in sorted_groups:
            result.extend(group_to_items[group_id])
        return result