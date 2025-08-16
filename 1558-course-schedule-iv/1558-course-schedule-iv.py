class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = collections.defaultdict(set)
        adj = collections.defaultdict(list)
        for pre, course in prerequisites:
            adj[course].append(pre)
        def dfs(course):
            if course not in pre_map:
                for nei in adj[course]:
                    pre_map[course] |= dfs(nei)
                pre_map[course].add(course)
            return pre_map[course]
        for i in range(numCourses):
            dfs(i)
        result = []
        for u, v in queries:
            result.append(u in pre_map[v])
        return result
        