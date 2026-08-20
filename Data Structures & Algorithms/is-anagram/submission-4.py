class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapp = {}
        for letter in s:
            if letter in mapp:
                mapp[letter] += 1
            else:
                mapp[letter] = 1
        
        for letter in t:
            if letter in mapp:
                mapp[letter] -= 1
            else:
                return False
        
        for k,v in mapp.items():
            if v != 0:
                return False
        return True