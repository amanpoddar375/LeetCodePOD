class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int count = 0;
        int length = strs[0].size();
        for(int col = 0 ; col< length ; col++){
            for(int row = 1; row < strs.size(); row++){
                if(strs[row][col] < strs[row-1][col]){
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};
