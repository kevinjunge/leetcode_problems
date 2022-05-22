# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()

    for i in range(len(nums)):
        if i == 0:
            prev = nums[i]
            continue
        if nums[i] == prev:
            return True
        prev = nums[i]

    return False
        
