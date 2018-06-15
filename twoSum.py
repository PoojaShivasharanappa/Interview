
'''
Brute Force method
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]



#Dictionary
class Solution:
    def twoSum(self,nums,target):
        numDict = {}
        for index,value in enumerate(nums):
            numDict[value]= index

        for index,value in enumerate(nums):
            if target - value in numDict and numDict[target-value] != index:
                return [index,numDict[target-value]]

 '''
