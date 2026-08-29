class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<int, int> m = {};
        int left = 0;
        int max_freq = 0;
        int max_len = 0;

        for(int right = 0; right < s.size(); right++){
            m[s[right]]++;
            max_freq = max(max_freq, m[s[right]]);

            int r = (right - left + 1) - max_freq;

            if(r > k){
                m[s[left]]--;
                left++;
            }
            
            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};
