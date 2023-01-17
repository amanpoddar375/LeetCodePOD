class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int countFlips = 0;
        int countOnes = 0;
        for(auto bit: s){
            if(bit == '1'){
                countOnes++;
            }
            else if(countOnes){
                countOnes -= 1;
                countFlips += 1;
            }
        }
        return countFlips;
    }
};
