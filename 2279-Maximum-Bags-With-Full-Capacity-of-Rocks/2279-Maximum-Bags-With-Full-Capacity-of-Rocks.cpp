class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int count = 0;
        int n = capacity.size();
        vector<int>fullBags(n);
        for (int i = 0; i < n; i++) {
            fullBags[i] = capacity[i] - rocks[i];
            }
        sort(fullBags.begin(), fullBags.end());
        for(auto x: fullBags){
            if(additionalRocks >= x){
                additionalRocks -= x;
                count ++;
            }
        }
        return count;
    }
};

//TC = O(n) because it loops through all the bags once.
//SC = O(1) because it only uses a constant number of variables.
