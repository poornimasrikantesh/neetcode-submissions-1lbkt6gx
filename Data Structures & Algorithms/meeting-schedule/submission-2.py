"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
      length = len(intervals)

      for i in range(length):
        A = intervals[i]
        for j in range(i+1, length):
          B=intervals[j]
          if max(A.start, B.start) < min(A.end, B.end):
            return False
      return True      
