class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashing=defaultdict(int)
        for num in arr:
            if num in arr:
                hashing[num]+=1
            else:
                hashing[num]=1
        lst=[i for i in hashing.values()]
        return True if len(lst)==len(set(lst)) else False