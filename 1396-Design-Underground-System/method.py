class UndergroundSystem:

    def __init__(self):
        
        self.checkin = {}
        self.travelTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        startStation, startTime = self.checkin[id]
        travelTime = t - startTime
        key = (startStation, stationName)
        if key in self.travelTime:
            totalTime, count = self.travelTime[key]
            self.travelTime[key] = (totalTime + travelTime, count+1)
        else:
            self.travelTime[key] = (travelTime, 1)
        del self.checkin[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        key = (startStation, endStation)
        totalTime, count = self.travelTime[key]
        return totalTime/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# TC : O(1)
# SC : O(1)
# The TC and SC of all the methods are constant because they perform a fixed number of operations regardless of the input size


