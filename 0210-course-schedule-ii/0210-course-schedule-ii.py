class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preq_dict = collections.defaultdict(list)

        for courses in prerequisites :
            trg_course, preq_course = courses
            preq_dict[trg_course].append(preq_course)

        def searchDFS(course, visited) :
            if visited[course] == -1:
                return False
            if visited[course] == 1 :
                return True
            visited[course] = -1
            for preq_course in preq_dict[course] :
                if not searchDFS(preq_course, visited) :
                    return False
            result.append(course)
            visited[course] = 1
            return True

        result = []
        visited = [0 for _ in range(numCourses)]
        for course_num in range(numCourses) :
            if not searchDFS(course_num, visited) :
                return []
        return result
