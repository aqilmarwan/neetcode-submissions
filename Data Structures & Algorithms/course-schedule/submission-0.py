class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)

            for pre in preMap[course]:
                if not dfs(pre):  
                    return False
            visitSet.remove(course)
            #pre-set the preMap so we dont have to run dfs again for 2nd time input queried
            preMap[course] = []
            return True

            # checks graph validity 1 ->2, 3 -> 4
            for course in range(numCourses):
                if not dfs(course): 
                    return False
                return True