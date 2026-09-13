"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # check if no 2nd start time in between first time nterval, 
        # if start_2 >= end_1 == conflict
        # elif continue

        intervals.sort(key=lambda i: i.start)
        
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end >= i2.start:
                return False
        return True