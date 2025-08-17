class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, cycle = set(), set()
        adj = collections.defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            cycle.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True    