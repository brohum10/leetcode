class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_Map = {} # index->value

        for index,value in enumerate(nums): #enumerate adding index and value

            if (target - value) in hash_Map: #if number needed in hashmap

                return [hash_Map[target - value], index]

            hash_Map[value] = index #adding it as inverse to hasmap

