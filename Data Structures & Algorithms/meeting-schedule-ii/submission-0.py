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
        # times.sort()
        print(times)
        return 0
        