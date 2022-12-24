class Solution {
public:
    int numTilings(int n) {
        if (n == 1) {
            return 1;
        }
        
        const int mod = 1000000007;
        vector<long long> dp(n, 0);
        vector<long long> dp_incomp(n, 0);
        
        dp[0] = 1;
        dp[1] = 2;
        dp_incomp[1] = 2;
        
        for (int i = 2; i < n; i++) {
            dp[i] =( dp[i - 2] + dp[i - 1] + dp_incomp[i - 1]) % mod;
            dp_incomp[i] = (dp[i - 2] * 2 + dp_incomp[i - 1])% mod;
        }
        
        return dp[n - 1] % mod;
    }
};
