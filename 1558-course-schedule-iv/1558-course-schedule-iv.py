class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = collections.defaultdict(set)
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            pre_map[pre[0]].add(pre[1])
            graph[pre[0]].append(pre[1])
        def dfs(course, neighbor, visited):
            if neighbor in visited:
                return
            visited.add(neighbor)
            if neighbor not in pre_map[course]:
                pre_map[course].add(neighbor)
            for nei in graph[neighbor]:
                dfs(course, nei, visited)
        for course in range(numCourses):
            dfs(course, course, set())
        result = []
        for query in queries:
            result.append(query[1] in pre_map[query[0]])
        return result