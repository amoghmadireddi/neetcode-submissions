#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> seen;
        if (s.length() != t.length()){
            return false;
        }
        for(int i = 0; i < s.length(); i++){
            seen[s[i]]++;
        }
        for(int i = 0; i < t.length(); i++){
            if (seen.find(t[i]) == seen.end()){
                return false;
            }
            if (seen[t[i]] == 0){
                return false;
            }
            seen[t[i]]--;
        }
        return true;
    }
};
