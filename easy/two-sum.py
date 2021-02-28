# O(n) complexity - iterate through the array once
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dictNums = {}
    for pos in range(0, len(nums)):
        complement = target - nums[pos]
        if (complement in dictNums):
            return [dictNums[complement],pos]
        dictNums[nums[pos]] = pos
    return [-1,-1]



# O(n^2) time complexity
def solution(arr, target):
    pos1 = pos2 = -1
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j] == target):
                return [i,j]
    return [-1,-1]