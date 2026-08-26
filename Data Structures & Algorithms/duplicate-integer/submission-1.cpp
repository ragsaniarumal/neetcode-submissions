class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mapp;

        for(int num : nums){
            mapp[num]++;
        }

        for(auto& [num, freq] : mapp){
            if(freq != 1){
                return true;
            }
        }
        return false;
    }
};