class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         dist={i:[] for i in range(numCourses)}
#         # course={i:0 for i in range(numCourses)}
#         for pre,cour in prerequisites:
#             dist[cour].append(pre)
#             # course[pre]+=1
#         visited=[0]*numCourses
#         res=[]
#         def dfs(i):
#             if visited[i] == 1:
#                 return True  # Cycle detected
#             if visited[i] == 2:
#                 return False  # Already processed, no cycle

#             visited[i] = 1  # Mark the course as visiting (in the current DFS path)
#             for neigh in dist[i]:
#                 if visited[neigh] == 0:  # If the neighbor is unvisited
#                     if dfs(neigh):  # If a cycle is detected in the neighbor, return True
#                         return True

#             visited[i] = 2  # Mark the course as visited (processed)
#             res.append(i)  # Add the course to result after processing all its prerequisites
#             return False

#         # Perform DFS for each course
#         for i in range(numCourses):
#             if visited[i] == 0:  # If the course hasn't been visited yet
#                 if dfs(i):  # If a cycle is detected, return []
#                     return []

#         return res[::-1]  # Reverse the result to get the correct topological order

        
#         # queue=deque(i for i in range(numCourses) if course[i]==0)
#         # res=[]
#         # while queue:
#         #     cor=queue.popleft()
#         #     res.append(cor)
#         #     for neighbour in dist[cor]:
#         #         course[neighbour]-=1
#         #         if course[neighbour]==0:
#         #             queue.append(neighbour)
                    
#         # if len(res) == numCourses:
#         #     return res
#         # else:
#         #     return []


        def dfs(sv,visited):
            if visited[sv]==-1:# this course had not been added into the res, but visited again; there is a cycle!
                return False
            if visited[sv]==1:# this course had been successfully added into the res
                return True
            visited[sv]=-1 # set the current course as currently being visited
            for u in adj[sv]:
                if not dfs(u,visited):
                    return False # if there is a cycle detected at any point, terminate!
            res.append(sv) # no cycle found, dfs finished, good to add the course into the res
            visited[sv]=1  # this course finished
            return True
        
        adj=[[] for i in range(numCourses)]
        res=[]
        for u,v in prerequisites:
            adj[v].append(u)
        visited=[0]*numCourses
        for i in range(numCourses):
            if not dfs(i,visited):
                # if False, there must be a cycle; terminate by returning an empty list
                return []
        return res[::-1]