class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos=(dividend<0) is (divisor<0)
        dividend, divisor = abs(dividend), abs(divisor) 
        res=0
        while dividend>=divisor:
            cur_d=divisor
            divi=1
            while dividend>=cur_d:
                dividend-=cur_d
                res+=divi
                cur_d<<=1
                divi<<=1
        if not pos:
            res=-res
        return max(min(2**31-1,res),-2**31)
                
            