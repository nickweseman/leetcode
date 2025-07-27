class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = collections.defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        cycle, visited = set(), set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            output.append(course)
            visited.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output