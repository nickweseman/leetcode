class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
        cycle, visited = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True