class Solution {
public:
    
    int getRotationAngle(vector<int> A, vector<int> B, vector<int> C) {
        return ((C[1] - A[1]) * (B[0] - A[0])) - ((B[1] - A[1]) * (C[0] - A[0]));
    }
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        if (trees.size() <= 3) return trees;
        
        sort(trees.begin(), trees.end());
        
        vector<vector<int>> upper;
        upper.push_back(trees[0]);
        upper.push_back(trees[1]);
        
        for(int i = 2; i< trees.size(); i++){
            int u = upper.size();
            
            while(u>= 2 && getRotationAngle(upper[u-2], upper[u-1], trees[i]) > 0){
                upper.pop_back();
                u--;
            }
            upper.push_back(trees[i]);
        }
        vector<vector<int>> lower;
        lower.push_back(trees[trees.size() - 1]);
        lower.push_back(trees[trees.size() - 2]);
        
        for(int i = trees.size() - 3; i >= 0; --i){
            int l = lower.size();
            
            while(l >= 2 && getRotationAngle(lower[l-2], lower[l-1], trees[i]) > 0){
                lower.pop_back();
                l--;
            }
            lower.push_back(trees[i]);
        }
        upper.insert(upper.end(), lower.begin(), lower.end());
        sort(upper.begin(), upper.end());
        upper.erase(unique(upper.begin(), upper.end()), upper.end());
        
        return upper;
    }
};

//Time Complexity : O(NlogN)
//Space Complexity : O(N)
