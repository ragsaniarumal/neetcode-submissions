class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mapp;

        for(int i=0; i<nums.size(); i++){

            int needed = target - nums[i];

            if(mapp.find(needed) != mapp.end()){
                return {mapp[needed], i};
            }

            mapp[nums[i]] = i;
        }

        return {};
    }
};
