# https://leetcode.com/problems/binary-search/

def search(nums: List[int], target: int):

    l, r = 0, len(nums) -1

    while(l <= r):
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid -1

    return -1
