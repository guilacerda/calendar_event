from datetime import datetime

class Event:
    def __init__(self, start, end, previous=None):
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise TypeError(
                "an event must consist of tuples of (datetime.datetime, datetime.datetime)"
            )

        if start >= end:
            raise ValueError("start could not be less than end")

        self.start = start
        self.end = end
        self.next = None
        self.previous = previous

    def __repr__(self) -> str:
        return f"{self.start} <> {self.end}"