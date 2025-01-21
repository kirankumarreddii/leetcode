class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # in_adj={i:[] for i in range(numCourses)}
        # courses={i:0 for i in range(numCourses)}
        # for cour,pre in prerequisites:
        #     in_adj[pre].append(cour)
        #     courses[cour]+=1
        # queue=deque(i for i in courses if courses[i]==0)
        # completed_course=0
        # while queue:
        #     cour=queue.popleft()
        #     completed_course+=1
        #     for c in in_adj[cour]:
        #         courses[c]-=1
        #         if courses[c]==0:
        #            queue.append(c)

        # if  completed_course==numCourses:
        #     return True
        # else:
        #     return False
        in_adj=defaultdict(list)
        for cour,pre in prerequisites:
            in_adj[pre].append(cour)
        visited=[0]*numCourses

        def dfs(visited,cours):
            if visited[cours]==1:
                return True
            if visited[cours]==2:
                return False
            visited[cours]=1
            for c in in_adj[cours]:
                if dfs(visited,c):
                    return True
            visited[cours]=2
            return False
        for cours in range(numCourses):
            if visited[cours]==0:
                if dfs(visited,cours):
                    return False
        return True
        
        