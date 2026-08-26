class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mapp;

        for(int num : nums){
            mapp[num]++;
        }

        vector<int> l;

        for (auto& [num, freq] : mapp) {
            l.push_back(num);
        }

        sort(l.begin(), l.end(), [&](int a, int b) {
            return mapp[a] > mapp[b];
        });

        return vector<int>(l.begin(), l.begin() + k);
    }
};
