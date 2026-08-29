class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int max_len = 0;
        unordered_map<int, int> m = {};

        for(int right = 0; right < s.size(); right++){
            char ch = s[right];

            if(m.find(ch) != m.end() and m[ch] >= left){
                left = m[ch] + 1;
            }
            m[ch] = right;
            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};
