class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> m;
        unordered_set<int> s;
        for(auto i: arr) m[i]++;
        for(auto& j: m) s.insert(j.second);
        return m.size() == s.size();
    }
};