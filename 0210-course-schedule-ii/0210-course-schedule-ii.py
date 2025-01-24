class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dist={i:[] for i in range(numCourses)}
        # course={i:0 for i in range(numCourses)}
        for pre,cour in prerequisites:
            dist[cour].append(pre)
            # course[pre]+=1
        visited=[0]*numCourses
        res=[]
        def dfs(i,visited):
            if visited[i] == 1:
                return True  # Cycle detected
            if visited[i] == 2:
                return False  # Already processed, no cycle

            visited[i] = 1  # Mark the course as visiting (in the current DFS path)
            for neigh in dist[i]:
                if dfs(neigh, visited):# If a cycle is detected in the neighbor, return True
                    return True

            visited[i] = 2  # Mark the course as visited (processed)
            res.append(i)  # Add the course to result after processing all its prerequisites
            return False

        # Perform DFS for each course
        for i in range(numCourses):
            if dfs(i,visited):  # If a cycle is detected, return []
                return []

        return res[::-1]  # Reverse the result to get the correct topological order

        
        # queue=deque(i for i in range(numCourses) if course[i]==0)
        # res=[]
        # while queue:
        #     cor=queue.popleft()
        #     res.append(cor)
        #     for neighbour in dist[cor]:
        #         course[neighbour]-=1
        #         if course[neighbour]==0:
        #             queue.append(neighbour)
                    
        # if len(res) == numCourses:
        #     return res
        # else:
        #     return []
