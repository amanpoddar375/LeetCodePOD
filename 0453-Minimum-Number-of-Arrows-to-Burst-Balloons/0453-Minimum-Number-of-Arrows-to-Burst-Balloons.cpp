class Solution {
 public:
  int findMinArrowShots(vector<vector<int>>& points) {
    int ans = 1;
    int endpoint = INT_MAX;
    sort(points.begin(), points.end());
    for (const auto& point : points) {
      int start = point[0];
      int end = point[1];
      if (endpoint < start) {
        ans++;
        endpoint = end;
      } 
      else {
        endpoint = min(endpoint, end);
      }
    }
    return ans;
  }
};
