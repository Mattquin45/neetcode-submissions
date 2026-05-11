class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, y in enumerate(nums):
            differ = target - y
            if differ in hashmap:
                return [hashmap[differ], i]
            else:
                hashmap[y] = i

        return []
        