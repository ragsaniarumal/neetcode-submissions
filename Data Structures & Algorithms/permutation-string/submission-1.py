class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0]*26
        count2 = [0]*26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        
        window_size = len(s1)

        for i in range(window_size):
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1 == count2:
            return True
        
        i = window_size

        while i < len(s2):
            count2[ord(s2[i]) - ord('a')] += 1
            j = i - window_size
            count2[ord(s2[j]) - ord('a')] -= 1
            if count1 == count2:
                return True
            i += 1
        
        return False