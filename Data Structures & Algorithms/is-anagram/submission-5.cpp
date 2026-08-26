class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int, int> mapp;

        for(auto ch : s){
            mapp[ch]++;
        }

        for(auto ch : t){
            mapp[ch]--;
        }

        for(auto& [ch, freq] : mapp){
            if(freq != 0){
                return false;
            }
        }

        return true;
    }
};
