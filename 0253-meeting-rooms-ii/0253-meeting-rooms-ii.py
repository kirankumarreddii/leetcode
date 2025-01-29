class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted([x[0] for x in intervals])
        end=sorted([x[1] for x in intervals])
        max_rooms,count=0,0
        i,j=0,0

        while i<len(start) and j<len(end):
            if start[i]<end[j]:
                count+=1
                
                i+=1
            else:
                count-=1
                j+=1
            max_rooms = max(max_rooms, count)
        return max_rooms