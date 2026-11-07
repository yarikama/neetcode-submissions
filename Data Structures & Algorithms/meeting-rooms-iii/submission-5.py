from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # counter = [0] * n
        # rooms = [(0, room) for room in range(n)]
        # heapify(rooms)
        # heapify(meetings)

        # while meetings:
        #     # while room_end < meeting_start -> pop & push another
        #     while rooms[0][0] < meetings[0][0]:
        #         room_end, room = heappop(rooms)
        #         heappush(rooms, (meetings[0][0], room))

        #     room_end, room = heappop(rooms)
        #     meeting_start, meeting_end = heappop(meetings)
        #     counter[room] += 1
        #     room_end = max(meeting_start, room_end) + meeting_end - meeting_start
        #     heappush(rooms, (room_end, room))

        # res = 0
        # max_cnt = float("-inf")
        # for room in range(len(counter)):
        #     if counter[room] > max_cnt:
        #         max_cnt = counter[room]
        #         res = room

        # return res

        meetings.sort()
        free = list(range(n))
        busy = []
        count = [0] * n

        for start, end in meetings:
            # release the busy rooms if next meeting start later than them
            while busy and busy[0][0] <= start:
                room_end_time, room = heappop(busy)
                heappush(free, room)


            # there is free room -> pick small nums -> push back to busy
            if free:
                room = heappop(free)
                heappush(busy, (end, room))

            # there is only busy room -> choose the earliest one, update the busy one
            else:
                room_end_time, room = heappop(busy)
                heappush(busy, (room_end_time + end - start, room))
            
            count[room] += 1

        return count.index(max(count))







        