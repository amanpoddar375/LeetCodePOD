//**** Time Complexity : O(logn)**** : As the loop variables are divided by a constant amount.
class Solution {
public:
    bool isUgly(int n) {
        if(n<=0)  // n needs to be a positive integer if not return false
            return false;
        std::vector<int> v = { 2,3,5 };  // defining range of numbers to use in the for loop
        for (auto i : v)   //using range-for loop
            while(n%i==0) //dividing n to check if there are other prime factor
                n/=i;
        return n==1;
    }
};