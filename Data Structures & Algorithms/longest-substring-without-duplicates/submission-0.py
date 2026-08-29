class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        mapp = {}

        for right in range(len(s)):
            ch = s[right]

            if ch in mapp and mapp[ch] >= left:
                left = mapp[ch] + 1

            mapp[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len