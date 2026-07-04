class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> tracker;
        for(int i = 0; i < nums.size(); i++){
            if(tracker.find(nums[i]) != tracker.end()){
                return true;
            }
            tracker.insert(nums[i]);
        }
        return false;
    }
};
