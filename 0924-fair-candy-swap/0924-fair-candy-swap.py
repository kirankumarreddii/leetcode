class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        SumA=sum(aliceSizes)
        SumB=sum(bobSizes)
        diff=(SumB-SumA)//2
        setB=set(bobSizes)

        for a in aliceSizes:
            if a+diff in setB:
                return [a,a+diff]
        
        