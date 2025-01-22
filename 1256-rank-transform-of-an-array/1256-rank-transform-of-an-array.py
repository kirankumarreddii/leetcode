class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # if not arr:
        #     return []
        # ranks=[]
        # dist={}
        # sort_list=sorted(arr)
        # dist[sort_list[0]]=1
        # count=1
        # for i in range(1,len(arr)):
        #     if sort_list[i]>sort_list[i-1]:
        #         count+=1
        #     dist[sort_list[i]]=count
        # for i in range(len(arr)):
        #     ranks.append(dist[arr[i]])
        # return ranks
        if not arr:
            return []
        
        dist = {}
        sort_list = sorted(set(arr))  # Remove duplicates and sort
        count = 1
        
        for i in range(len(sort_list)):
            dist[sort_list[i]] = count
            count += 1  # Assign increasing ranks
        
        return [dist[num] for num in arr]  # Map original array values to their ranks
