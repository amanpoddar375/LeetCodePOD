class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int rows = maze.size();
        int columns = maze[0].size();
        queue<pair<int, int>>q;
        int steps = 0;
        
        vector<vector<int>>direction = {{0,1},{0,-1},{-1,0},{1,0}};
        q.push({entrance[0], entrance[1]});
        maze[entrance[0]][entrance[1]] = '+';
        
        while(!q.empty()){
            int l = q.size();
            steps++;
            for(int i = 0; i<l; i++){
                auto [x_cord,y_cord]=q.front();
                q.pop();
                for(int k = 0; k<4; k++){
                    int x = x_cord + direction[k][0];
                    int y = y_cord + direction[k][1];
                    
                    if(x<0 || y<0 || x>=rows || y>=columns || maze[x][y]=='+')
                        continue;
                    if(x==0 || y==0 || x==rows-1 || y==columns-1)
                        return steps;
                    maze[x][y]='+';
                    q.push({x,y});
                }
            }
        }
        return -1;
    }
};