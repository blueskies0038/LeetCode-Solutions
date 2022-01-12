class MyCalendar:
​
    def __init__(self):
        self.starts = []
        self.ends = []
​
    def book(self, start: int, end: int) -> bool:
        l = 0
        r = len(self.starts)
        while l < r:
            mid = l + (r - l) // 2
            if (start < self.starts[mid]):
                r = mid;
            else:
                l = mid + 1
        if l - 1 >= 0:
            if start < self.ends[l-1]:
                return False
        if l < len(self.starts):
            if end > self.starts[l]:
                return False
        self.starts.insert(l, start)
        self.ends.insert(l, end)
        return True
​
​
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
