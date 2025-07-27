class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = collections.defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            cycle.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            pre_map[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True