class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        int x1 = rec1[0], y1 = rec1[1], x2 = rec1[2], y2 = rec1[3];
	    int x3 = rec2[0], y3 = rec2[1], x4 = rec2[2], y4 = rec2[3];
        return ( min(x2,x4) > max(x1,x3) && min(y2,y4) > max(y1,y3));
    }
};