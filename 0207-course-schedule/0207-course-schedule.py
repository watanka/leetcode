class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preq_dic = collections.defaultdict(list)
        for preq in prerequisites :
            trg_cls, preq_cls = preq
            preq_dic[trg_cls].append(preq_cls)

        visited = [0 for _ in range(numCourses)]

        taken = set()
        def dfs(course) :
            if not preq_dic[course] :
                return True

            if course in taken :
                return False

            taken.add(course)

            for p in preq_dic[course] :
                if not dfs(p) :
                    return False
                
            preq_dic[course] = []
            return True


        for course in range(numCourses) :
            if not dfs(course) :
                return False
        return True

            