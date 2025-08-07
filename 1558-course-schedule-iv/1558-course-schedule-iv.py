class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = collections.defaultdict(set)
        adj = collections.defaultdict(list)
        for pre, course in prerequisites:
            adj[course].append(pre)
        def dfs(course):
            if course in pre_map:
                return pre_map[course]
            for nei in adj[course]:
                pre_map[course] |= dfs(nei)
            pre_map[course] |= {course}
            return pre_map[course]
        for course in range(numCourses):
            dfs(course)
        return [q[0] in pre_map[q[1]] for q in queries]
        