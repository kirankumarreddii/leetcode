class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashing=defaultdict(int)
        for num in arr:
            if num in arr:
                hashing[num]+=1
        return True if len(hashing.values())==len(set(hashing.values())) else False