class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        Array = []
        for n in strs:
            sorted_str = tuple(sorted(n))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(n)
            else:
                hashmap[sorted_str] = [n]
        return list(hashmap.values())