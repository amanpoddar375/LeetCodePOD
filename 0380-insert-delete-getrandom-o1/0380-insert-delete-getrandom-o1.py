class RandomizedSet:

    def __init__(self):
        self.data = []
        self.datamap = {}

    def insert(self, val: int) -> bool:
        if val not in self.datamap:
            self.data.append(val)
            self.datamap[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.datamap:
            i = self.datamap[val]
            l = self.data[-1]
            self.data[i] = l
            self.datamap[l] = i
            self.data.pop()
            self.datamap.pop(val,0)
            return True
        return False

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()