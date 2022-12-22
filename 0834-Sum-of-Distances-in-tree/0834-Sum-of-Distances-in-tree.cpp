class Solution {
 public:
  vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
    unordered_map<int, vector<int>> g;
    for (const auto& edge : edges) {
      g[edge[0]].push_back(edge[1]);
      g[edge[1]].push_back(edge[0]);
    }

    int ans = 0;
    unordered_map<int, int> subtree;

    function<int(int, int, int)> dfs = [&](int node, int prev, int depth) {
      int total = 1;
      ans += depth;
      for (int child : g[node]) {
        if (child == prev) continue;
        total += dfs(child, node, depth + 1);
      }
      subtree[node] = total;
      return total;
    };

    dfs(0, -1, 0);
    vector<int> res(n, 0);
    res[0] = ans;

    function<void(int, int)> dfs2 = [&](int node, int prev) {
      for (int child : g[node]) {
        if (child == prev) continue;
        res[child] = res[node] - subtree[child] + (n - subtree[child]);
        dfs2(child, node);
      }
    };

    dfs2(0, -1);
    return res;
  }
};
