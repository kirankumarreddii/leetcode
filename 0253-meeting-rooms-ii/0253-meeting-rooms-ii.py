class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # start=sorted([x[0] for x in intervals])
        # end=sorted([x[1] for x in intervals])
        # max_rooms,count=0,0
        # i,j=0,0

        # while i<len(start) and j<len(end):
        #     if start[i]<end[j]:
        #         count+=1  
        #         i+=1
        #     else:
        #         count-=1
        #         j+=1
        #     max_rooms = max(max_rooms, count)
        # return max_rooms
        meeting_room=[]
        intervals.sort(key= lambda x:x[0])
        heapq.heappush(meeting_room,intervals[0][1])

        for i in intervals[1:]:
            if i[0]>=meeting_room[0]:
                heapq.heappop(meeting_room)
            heapq.heappush(meeting_room,i[1])
        return len(meeting_room)