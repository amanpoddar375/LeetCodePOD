class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<vector<int>> all_paths;
        function<void(int, vector<int>)> dfs;
        dfs = [&](int node, vector<int> path) {
            if (node == n - 1) {
                all_paths.push_back(path);
                return;
            }
            for (int neighbor : graph[node]) {
                vector<int> new_path = path;
                new_path.push_back(neighbor);
                dfs(neighbor, new_path);
            }
        };
        dfs(0, {0});
        return all_paths;   
    }
};
