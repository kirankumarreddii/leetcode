class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return '0'
        res=''
        if (numerator<0) ^ (denominator<0):
            res+='-'
        numerator=abs(numerator) 
        denominator=abs(denominator)
        integer=numerator//denominator
        remainder=numerator%denominator
        if remainder==0:
            return res + str(integer)
        res += str(integer) + '.'
        position=0
        integer_part=''
        dist={}
        while remainder!=0:
            if remainder in dist:
                idx=dist[remainder]
                return res + integer_part[:idx] + '(' + integer_part[idx:] + ')'
                
            dist[remainder]=position
            remainder*=10
            integer_part+=str(remainder//denominator)
            remainder%=denominator
            position+=1
        return res + integer_part