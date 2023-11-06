class SeatManager(object):
    def __init__(self, n):
        self.arr = []
        self.v = 1
        heapq.heapify(self.arr)

    def reserve(self):
        if not self.arr:
            self.v += 1
            return self.v - 1
        else:
            return heapq.heappop(self.arr)

    def unreserve(self, seatNumber):
        heapq.heappush(self.arr, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
