class Solution {
public:
 int maxPoints(vector<vector<int>>& points) {
        int result = 1;
        for(int i=0;i<points.size()-1;i++){
        unordered_map<double,int>slopes;
            for(int j=i+1;j<points.size();j++){
                if(points[i][0] == points[j][0]){
                    slopes[1000001]++;
                }
                else{
                    double slope = (double)(points[j][1]-points[i][1])/(double)(points[i][0]-points[j][0]);
                    slopes[slope]++;
                }
            }
            int temp=0;
            for(auto x:slopes){
                temp = max(temp,x.second);
            }
            result = max(result,temp+1);
        }
        return result;
    }
};
// TC : O(n^2)-two loops
// SC : O(n), because the maximum number of elements in the map is equal to the number of points in the input.
