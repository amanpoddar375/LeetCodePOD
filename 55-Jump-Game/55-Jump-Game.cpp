class Solution {
public:
    bool canJump(vector<int>& nums) {
      int lastpos = 0;
      int n = nums.size();
      for(int i = 0; i<n; i++){
          if(i>lastpos){
              return false;
          }
          lastpos = max(lastpos, i + nums[i]);
      }
      return true; 
    }
};
