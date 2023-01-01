class Solution {
public:
    bool wordPattern(string pattern, string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        while(getline(ss,word, ' ')){
            words.push_back(word);
        }
        if(words.size() != pattern.size()){
            return false;
        }
        unordered_map<char, string> mapping;
        unordered_set<string> visited;
        for(int i = 0; i < pattern.size(); i++){
            char ch = pattern[i];
            string word = words[i];
            if(mapping.count(ch) == 0){
                if(visited.count(word) > 0){
                    return false;
                }
                mapping[ch] = word;
                visited.insert(word);
            }
            else if(mapping[ch] != word){
                return false;
            }
        }
        return true;
    }
}
