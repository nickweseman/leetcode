class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = collections.defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if len(prereq_map[course]) == 0:
                return True
            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course) # why?
            prereq_map[course] = [] # why?
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True