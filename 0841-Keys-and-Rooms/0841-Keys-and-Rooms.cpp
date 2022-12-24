class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        set<int> visited;
        stack<int> stack;
        stack.push(0);
        while (!stack.empty()) {
            int current_room = stack.top();
            stack.pop();
            if (visited.find(current_room) == visited.end()) {
                visited.insert(current_room);
                for (int room : rooms[current_room]) {
                    stack.push(room);
                }
            }
        }
        return visited.size() == rooms.size();
    }
};

/*The time complexity is O(N), where N is the total number of rooms.
This is because each room is visited and processed exactly once. */

/* The space complexity is  O(N), as the maximum size of the stack 
(and therefore the maximum number of rooms that can be stored on the stack at any given time) 
is equal to the total number of rooms. This is because in the worst case, all rooms are connected to the first room, 
and therefore all rooms will be added to the stack at some point */
