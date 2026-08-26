class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> mapp;

        for (string s : strs) {
            vector<int> count(26, 0);

            for (char c : s) {
                count[c - 'a']++;
            }

            mapp[count].push_back(s);
        }

        vector<vector<string>> ans;

        for (auto& pair : mapp) {
            ans.push_back(pair.second);
        }

        return ans;
    }
};
