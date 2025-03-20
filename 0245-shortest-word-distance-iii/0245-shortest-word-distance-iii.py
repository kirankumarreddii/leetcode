class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # store=defaultdict(list)
        # for i,val in enumerate(wordsDict):
        #     store[val].append(i)
        # mini=float('inf')
        # if word1==word2:
        #     indx=store[word1]
        #     for i in range(len(indx)-1):
        #         mini=min(mini,abs(indx[i+1]-indx[i]))
        # else:
        #     indx1=store[word1]
        #     indx2=store[word2]
        #     i=j=0
        #     while i<len(indx1) and j<len(indx2):
        #         mini=min(mini,abs(indx2[j]-indx1[i]))
        #         if indx1[i]<indx2[j]:
        #             i+=1
        #         else:
        #             j+=1

        # return mini
        index1=index2=-1
        mini=float('inf')
        for i,val in enumerate(wordsDict):
            if val==word1:
                if word2==word1:
                    index1=index2
                index2=i
            elif val == word2:
                index1=i
            if index1!=-1 and index2!=-1:
                mini=min(mini,abs(index2-index1))
        return mini

                

