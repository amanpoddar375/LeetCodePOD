class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        long target = skill[0] + skill[skill.size()-1];
        long sum = 0;
        int n = skill.size();
        for(int i = 0; i < n/2; i++){
            if(target != skill[i] + skill[n-i-1])
                return -1;
            sum += skill[i] * skill[n-i-1];
        }
        return sum;
    }
};
