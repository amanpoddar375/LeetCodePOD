class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        long long res = 0;
        vector<map<long long, int>>dp(n);
        for(int i = 1; i<n; i++){
            for(int j = 0; j<i; j++){
                long long d = (long long)nums[i] - (long long) nums[j];
                if(d<= INT_MIN || d >= INT_MAX){
                    continue;
                }
                int s = 0;
                if(dp[j].find(d) != dp[j].end()){
                    s = dp[j][d];
                }
                dp[i][d] += s + 1;
                res += s;
            }
        }
        return (int)res;
    }
};