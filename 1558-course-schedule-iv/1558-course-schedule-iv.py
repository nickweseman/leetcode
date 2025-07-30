class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = collections.defaultdict(set)
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        def dfs(course, neighbor, visited):
            if neighbor in visited:
                return
            visited.add(neighbor)
            pre_map[course].add(neighbor)
            for nei in graph[neighbor]:
                dfs(course, nei, visited)
        for course in range(numCourses):
            dfs(course, course, set())
        result = []
        for query in queries:
            result.append(query[0] in pre_map[query[1]])
        return result