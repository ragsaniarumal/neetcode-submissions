class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> prefix(n, 0);
        vector<int> suffix(n, 0);
        int curr_max = 0;
        int water = 0;

        for(int i = 0; i < n; i++){
            curr_max = max(height[i], curr_max);
            prefix[i] = curr_max;
        }

        curr_max = 0;
        
        for(int j = n - 1; j >= 0; j--){
            curr_max = max(height[j], curr_max);
            suffix[j] = curr_max;
        }

        for(int i = 0; i < n; i++){
            water += min(prefix[i], suffix[i]) - height[i];
        }

        return water;
    }
};
