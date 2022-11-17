class Solution {
public:
    bool checkOverlapping(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2){
        return ( min(ax2,bx2) > max(ax1,bx1) && min(ay2,by2) > max(ay1,by1));
    }
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int a1,a2,a3, result;
        a1 = abs(ax2 - ax1) * abs(ay2 - ay1);
        a2 = abs(bx2 - bx1) * abs(by2 - by1);
        
        bool check = checkOverlapping(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2);
        if(!check){
            return result = a1 + a2;
        }
        else{
            int x = min(ax2,bx2) - max(ax1,bx1);
            int y = min(ay2,by2) - max(ay1,by1);
            result = a1 + a2 - x*y;
        }
        
        return result;
    }
};