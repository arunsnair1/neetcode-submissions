class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        prev = intervals[0].end

        for meeting in intervals[1:]:

            if meeting.start < prev:
                return False

            prev = meeting.end

        return True