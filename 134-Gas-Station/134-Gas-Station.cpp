class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalg = 0;
        int currg = 0;
        int startInd = 0;
        for(int i = 0; i< gas.size(); i++){
            currg += gas[i] - cost[i];
            totalg += gas[i] - cost[i];
            if(currg < 0){
                startInd = i+1;
                currg = 0;
            }
        }
        return totalg >= 0 ? startInd : -1;
    }
};
