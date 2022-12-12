class Solution {
public:
    int climbStairs(int n) {
        if(n<=0) return 0;
        if(n == 1) return 1;
        if(n== 2) return 2;

        int onestep = 2;
        int twosteps = 1;
        int result = 0;
        for(int i=2; i<n; i++){
            result = onestep + twosteps;
            twosteps = onestep;
            onestep = result;

        }
        return result;
    }
};
