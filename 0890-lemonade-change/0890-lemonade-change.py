class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5=0
        count_10=0
        for num in bills:
            if num==5:
                count_5+=1
            elif num==10:
                if count_5>0:
                    count_10+=1
                    count_5-=1
                else:
                    return False
            else:
                if count_5>0 and count_10>0:
                    count_10-=1
                    count_5-=1
                elif count_5>2:
                    count_5-=3
                else:
                    return False
        return True