class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = dict()
        for n in s:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        for num in t:
           if num in hashmap:
            hashmap[num] -= 1
           else:
            return False 
        
        for Val in hashmap.values():
            if Val != 0:
                return False

        return True

        