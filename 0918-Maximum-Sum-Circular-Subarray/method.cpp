class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int max_sum, curr_max, min_sum, curr_min;
        max_sum = curr_max = min_sum = curr_min = nums[0];
        int total_sum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            total_sum += nums[i];
            curr_max = max(nums[i], curr_max + nums[i]);
            max_sum = max(max_sum, curr_max);
            curr_min = min(nums[i], curr_min + nums[i]);
            min_sum = min(min_sum, curr_min);
        }
        return max_sum > 0 ? max(max_sum, total_sum - min_sum) : max_sum;
    }
};
