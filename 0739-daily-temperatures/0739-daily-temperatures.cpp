class Solution {
public:
    vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        vector<int> result(temperatures.size(), 0);
        vector<int> stack;
        stack.reserve(temperatures.size());
        for (int i = 0; i < temperatures.size(); i++) {
            while (!stack.empty() && temperatures[stack.back()] < temperatures[i]) {
                result[stack.back()] = i - stack.back();
                stack.pop_back();
            }
            stack.push_back(i);
        }
        return result;
    }
};
//time complexity = O(n) 
//space complexity = O(n)
