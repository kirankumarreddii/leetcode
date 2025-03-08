class Solution:
    def countElements(self, arr: List[int]) -> int:
        numbers=0
        count={}
        for num in arr:
            if num not in count:
                count[num]=0
            count[num]+=1
        print(count)
        for num in arr:
            if num+1 in count:
                numbers+=1
        return numbers
            
