class Solution:
    def binaryGap(self, n: int) -> int:
        binary=format(n,'b')
        distance=0
        once=1
        for i in range(1,len(binary)):
            if binary[i]=='1':
                distance=max(distance,i+1-once)
                once=i+1
        return distance

