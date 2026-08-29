class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int best_price = prices[0];

        for(auto price : prices){
            best_price = min(best_price, price);
            max_profit = max(max_profit, price - best_price);
        }

        return max_profit;
    }
};
