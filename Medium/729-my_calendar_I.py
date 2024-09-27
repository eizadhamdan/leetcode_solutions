class MyCalendar:

    def __init__(self):
        self.interval = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.interval:
            if start < e and end > s:
                return False
        
        self.interval.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)