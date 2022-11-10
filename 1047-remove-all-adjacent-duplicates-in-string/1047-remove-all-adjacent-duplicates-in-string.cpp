class Solution {
public:
    string removeDuplicates(string s) {
        string inp;
        for(int i = 0; i < s.size(); i++){
            if(inp.back()== s[i]){
                inp.pop_back();
            }
            else{
                inp += s[i];
            }
        }
        return inp;
    }
};