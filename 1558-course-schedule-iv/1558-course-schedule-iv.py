class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)
        for pre, course in prerequisites:
            graph[course].append(pre)
        def dfs(course):
            if course not in pre_map:
                pre_map[course] = set()
                for pre in graph[course]:
                    pre_map[course] |= dfs(pre) # set union
                pre_map[course].add(course)
            return pre_map[course]
        pre_map = {}
        for course in range(numCourses):
            dfs(course)
        result = []
        for u, v in queries:
            result.append(u in pre_map[v])
        return result