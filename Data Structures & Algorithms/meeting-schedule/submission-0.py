"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = [ (interval.start, True) for interval in intervals ] + [ (interval.end, False) for interval in intervals ]
        times.sort()

        pre = None
        for _, is_start in times:
            if pre == is_start:
                return False
            pre = is_start

        return True