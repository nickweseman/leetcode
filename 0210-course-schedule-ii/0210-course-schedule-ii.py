class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        cycle = set()
        visited = set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output