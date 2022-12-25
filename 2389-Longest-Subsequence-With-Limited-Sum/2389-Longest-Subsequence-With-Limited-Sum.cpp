class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        vector<int> result;
        for (int query : queries) {
            int count = 0;
            int total = 0;
            for (int num : nums) {
                total += num;
                count++;
                if (total > query) {
                    count--;
                    break;
                }
            }
            result.push_back(count);
        }
        
        return result;
    }
};

/* The time complexity is O(nm log n), where n is the length of the nums array and m is the length of the queries array.
This is because the solution first sorts the nums array in non-decreasing order, which takes O(n log n) time,
and then it iterates through each query and each element in the nums array, which takes O(nm) time.*/

/*The space complexity of the solution is O(m), where m is the length of the queries array.
This is because the solution creates a new vector to store the result, which takes O(m) space*/
