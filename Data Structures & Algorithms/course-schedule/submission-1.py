class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}

        for req in prerequisites:
            if req[0] not in courseMap:
                courseMap[req[0]] = []
            if req[1] not in courseMap:
                courseMap[req[1]] = []
            courseMap[req[0]].append(req[1])

        print(courseMap)

        def dfs(course:str, courseSet: set) -> bool:
            if not courseMap[course]:
                return True
            for req in courseMap[course]:
                if req in courseSet:
                    return False
                courseSet.add(req)
                if not dfs(req, courseSet):
                    return False
                courseSet.remove(req)
                courseMap[req] = []
            return True

        for course in courseMap:
            courseSet = set()
            courseSet.add(course)
            if not dfs(course, courseSet):
                return False

        return True