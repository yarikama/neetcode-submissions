from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counter = [0] * n
        rooms = [(0, room) for room in range(n)]
        heapify(rooms)
        heapify(meetings)

        while meetings:
            # while room_end < meeting_start -> pop & push another
            while rooms[0][0] < meetings[0][0]:
                room_end, room = heappop(rooms)
                heappush(rooms, (meetings[0][0], room))

            room_end, room = heappop(rooms)
            meeting_start, meeting_end = heappop(meetings)
            counter[room] += 1
            room_end = max(meeting_start, room_end) + meeting_end - meeting_start
            heappush(rooms, (room_end, room))

        res = 0
        max_cnt = float("-inf")
        for room in range(len(counter)):
            if counter[room] > max_cnt:
                max_cnt = counter[room]
                res = room

        return res







        