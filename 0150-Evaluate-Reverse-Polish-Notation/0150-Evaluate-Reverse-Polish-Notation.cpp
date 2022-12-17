class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (const string& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                long long b = s.top(); s.pop();
                long long a = s.top(); s.pop();
                if (t == "+") s.push(a + b);
                else if (t == "-") s.push(a - b);
                else if (t == "*") s.push(a * b);
                else s.push(a / b);
            } else s.push(stoi(t));
        }
        return s.top();
    }
};
