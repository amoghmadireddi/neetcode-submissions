class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mapper;
        vector<int> returns;
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(mapper.find(diff) != mapper.end()){
                returns.push_back(mapper[diff]);
                returns.push_back(i);
                return returns;
            }
            mapper[nums[i]] = i;
        }
        return returns;
    }
};
