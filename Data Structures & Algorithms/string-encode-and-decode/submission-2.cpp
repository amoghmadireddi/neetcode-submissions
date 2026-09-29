class Solution {
public:

    string encode(vector<string>& strs) {
        string returner = "";
        for(int i = 0; i < strs.size(); i++){
            returner += std::to_string(strs[i].length()) + "#" + strs[i];
        }
        return returner;
    }

    vector<string> decode(string s) {
        vector<string> returns;
        for(int i = 0; i < s.length();){
            int j = 0;
            while(s[i + j] != '#'){
                j++;
            }
            int string_len = std::stoi(s.substr(i, j));
            std::cout << string_len << std::endl;
            returns.push_back(s.substr(i + j + 1, string_len));
            i = i + j + 1 + string_len;
        }
        return returns;
    }
};
