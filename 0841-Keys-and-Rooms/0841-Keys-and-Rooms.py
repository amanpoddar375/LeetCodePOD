class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            current_room = stack.pop()
            if current_room not in visited:
                visited.add(current_room)
                stack.extend(rooms[current_room])
        return len(visited) == len(rooms)
