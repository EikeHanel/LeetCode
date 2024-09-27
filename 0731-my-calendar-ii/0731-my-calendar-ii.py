class MyCalendarTwo:

    def __init__(self):
        self.event = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if not (end <= s or e <= start):
                return False

        for s, e in self.event:
             if not (end <= s or e <= start):
                self.overlap.append(
                    (max(s, start), min(e, end))
                    )
        self.event.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)