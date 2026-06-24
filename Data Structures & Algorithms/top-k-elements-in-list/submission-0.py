class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashmap = dict()
        array = []

        for n in nums:
            Hashmap[n] = 1 + Hashmap.get(n,0)
        
        freq = [[] for i in range(len(nums)+ 1)]
        
        for num, count in Hashmap.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq) -1, 0, -1):
            for nums in freq[i]:
                res.append(nums)
                if len(res) == k:
                    return res


        