class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        long totalsum = 0, currentsum = 0;
        int n = nums.size();
        for(int i = 0; i<n;i++){
            totalsum += nums[i];
        }
        int minsum = INT_MAX;
        int answerIndex = 0;
        for(int i = 0; i< n; i++){
            currentsum += nums[i];
            long fpavg = currentsum/(i+1);
            
            
            if(i == n-1){
                if(fpavg<minsum)
                    return n-1;
                else
                    break;
            }
            long spavg = (totalsum - currentsum)/(n-i-1);
            long diff = abs(fpavg - spavg);
            if(diff< minsum){
                minsum = diff;
                answerIndex = i;
            }
        }
        return answerIndex;
    }
};