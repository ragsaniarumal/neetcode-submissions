class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size()){
            return false;
        }

        vector<int> count1(26,0);
        vector<int> count2(26,0);

        for(auto ch : s1){
            count1[ch - 'a']++;
        }

        int window_size = s1.size();

        for(int i = 0; i < window_size; i++){
            count2[s2[i] - 'a']++;
        }

        if(count1 == count2){
            return true;
        }

        for(int i = window_size; i < s2.size(); i++){
            count2[s2[i] - 'a']++;
            int j = i - window_size;
            count2[s2[j] - 'a']--;

            if(count1 == count2){
                return true;
            }
        }

        return false;
    }
};
