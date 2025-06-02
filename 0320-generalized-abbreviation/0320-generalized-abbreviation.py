class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res=[]
        def generate(cur,index,count):
            if len(word)==cur:
                if count>0:
                    index+=str(count)
                res.append(index)
                return


            generate(cur+1,index,count+1)
            new_cur=index
            if count>0:
                new_cur += str(count)
            new_cur += word[cur]
            generate(cur+1,new_cur,0)


        generate(0,"",0)
        return res