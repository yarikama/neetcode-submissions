"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = [(interval.start, True) for interval in intervals] + [(interval.end, False) for interval in intervals]
        times.sort()

        cur_room_cnt, max_room_cnt = 0, 0
        for _, is_start in times:
            if is_start:
                cur_room_cnt += 1
            else:
                cur_room_cnt -= 1
            max_room_cnt = max(max_room_cnt, cur_room_cnt)
        return max_room_cnt
        