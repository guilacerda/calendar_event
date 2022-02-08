from .event import Event


class BusyEvent:
    def __init__(self, events=None):
        self.head = None
        self.tail = None
        events = events or []

        for event in events:
            self.add_event(event)

    def __iter__(self):
        event = self.head
        while event is not None:
            yield event
            event = event.next

    def add_event(self, event):
        _start, _end = event
        node_event = Event(start=_start, end=_end)

        if self.head is None:
            self.head = node_event
            self.tail = node_event
            return self

        if _start >= self.tail.start and _start < self.tail.end:
            self.tail.end = _end
        else:
            node_event.previous = self.tail
            self.tail.next = node_event
            self.tail = node_event

        return self

    def to_list(self):
        return [(event.start, event.end) for event in self if self.head]
