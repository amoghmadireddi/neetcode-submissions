class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix = nums;
        int tracker = 1;
        for(int i = 0; i < prefix.size(); i++){
            prefix[i] = tracker;
            tracker *= nums[i];
        }
        tracker = 1;
        for (int i = prefix.size() - 1; i >= 0; i--){
            prefix[i] *= tracker;
            tracker *= nums[i];
        }
        return prefix;
    }
};
