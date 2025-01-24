class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        