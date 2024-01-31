'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] == nums[j]:
                    return True
        return False
