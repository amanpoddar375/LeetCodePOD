class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]    # O(length)
        self.snap_id = 0        

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))     # O(1)
        

    def snap(self) -> int:
        self.snap_id += 1           # O(1)
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        values = self.arr[index]         # O(1)
        left, right = 0, len(values) - 1

        while left <= right:        # O(log n)
            mid = (left + right) // 2
            if values[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return values[right][1]     # O(1)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)