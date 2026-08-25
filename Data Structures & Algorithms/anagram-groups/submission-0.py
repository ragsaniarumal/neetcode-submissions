class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}

        for s in strs:
            char_arr = [0]*26
            for ch in s:
                char_arr[ord(ch) - ord('a')] += 1
            
            k = tuple(char_arr)

            if k not in mapp:
                mapp[k] = []

            mapp[k].append(s)
        
        return list(mapp.values())