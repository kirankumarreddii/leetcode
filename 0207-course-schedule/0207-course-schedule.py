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
        # in_adj=defaultdict(list)
        # for cour,pre in prerequisites:
        #     in_adj[pre].append(cour)
        # visited=[0]*numCourses

        # def dfs(visited,cours):
        #     if visited[cours]==1:
        #         return True
        #     if visited[cours]==2:
        #         return False
        #     visited[cours]=1
        #     for c in in_adj[cours]:
        #         if dfs(visited,c):
        #             return False
        #     visited[cours]=2
        #     return False
        # for cours in range(numCourses):
        #     if visited[cours]==0:
        #         if dfs(visited,cours):
        #             return False
        # return True
        
        
           
        in_adj = defaultdict(list)
        for cour, pre in prerequisites:
            in_adj[pre].append(cour)
        
        visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited (processed)
        
        def dfs(visited, cours):
            if visited[cours] == 1:  # Cycle detected (course is in progress)
                return True  # Return True if a cycle is detected
            if visited[cours] == 2:  # Already processed, no cycle
                return False  # Return False if no cycle is detected
            
            # Mark the course as visiting (in progress)
            visited[cours] = 1
            
            # Visit all the prerequisites (neighbors) of the course
            for c in in_adj[cours]:  # Iterate over all courses dependent on current course
                if dfs(visited, c):  # If a cycle is detected in the prerequisites
                    return True  # Return True if a cycle is detected
            
            # Mark the course as fully processed
            visited[cours] = 2
            return False  # Return False if no cycle was detected in the prerequisites
        
        # Perform DFS for each course
        for cours in range(numCourses):
            if visited[cours] == 0:  # If the course hasn't been visited yet
                if dfs(visited, cours):  # If a cycle is detected, return False
                    return False
        
        # If no cycle is detected, return True
        return True