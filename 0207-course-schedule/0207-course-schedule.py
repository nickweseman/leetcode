class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            graph[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            