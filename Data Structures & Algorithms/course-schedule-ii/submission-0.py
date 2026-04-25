class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i: [] for i in range(numCourses)}
        res = []
        visited, cycle = set(), set()

        for req in prerequisites:
            courseMap[req[0]].append(req[1])

        def dfs(course: int) -> bool:
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)
            for req in courseMap[course]:
                if not dfs(req):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
        