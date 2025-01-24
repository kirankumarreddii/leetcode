class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dist={i:[] for i in range(numCourses)}
        # for pre,cour in prerequisites:
        #     dist[cour].append(pre)
            
        # visited=[0]*numCourses
        # res=[]
        # def dfs(i):
        #     if visited[i]==1:
        #         return True
        #     if visited[i]==2:
        #         return False
        #     visited[i]=1
        #     for neigh in dist[i]:
        #         if dfs(neigh):
        #                 return True

        #     visited[i]=2
        #     res.append(i)
        #     return False
        # for i in range(numCourses):
        #         if dfs(i):
        #             return []
        # return res[::-1]


        dist={i:[] for i in range(numCourses)}
        course={i:0 for i in range(numCourses)}
        for pre,cour in prerequisites:
            dist[cour].append(pre)
            course[pre]+=1
        queue=deque(i for i in range(numCourses) if course[i]==0)
        res=[]
        while queue:
            cor=queue.popleft()
            res.append(cor)
            for neighbour in dist[cor]:
                course[neighbour]-=1
                if course[neighbour]==0:
                    queue.append(neighbour)
                    
        if len(res) == numCourses:
            return res
        else:
            return []

        