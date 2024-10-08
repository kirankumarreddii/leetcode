class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common=list(set(list1) & set(list2))
        d={}
        for i in common:
            d[i]=list1.index(i)+list2.index(i)
        m=min(d.values())
        op=[]
        for i in d:
            if d[i]==m:
                op.append(i)
        return op

