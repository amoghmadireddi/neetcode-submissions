class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        if(prices.size() == 0){
            return best;
        }
        int lowest = prices[0];
        for(int i = 1; i < prices.size(); i++){
            best = max(best, prices[i] - lowest);
            lowest = min(lowest, prices[i]);
        }

        return best;
    }
};
