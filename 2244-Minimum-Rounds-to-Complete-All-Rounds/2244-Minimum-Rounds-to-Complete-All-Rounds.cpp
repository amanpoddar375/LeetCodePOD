class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        // store the frequency in map
        unordered_map<int,int> frequency_count;
        for(int i=0;i<tasks.size();i++){
            frequency_count[tasks[i]]++;
        }
        int result = 0;
        for (auto [difficulty, count] : frequency_count) {
            if (count == 1) {
                return -1;
            } else if (count % 3 == 0) {
                result += count / 3;
            } else if (count % 3 == 1 || count % 3 == 2) {
                result += count / 3 + 1;
            }
        }
        return result;
    }
};
