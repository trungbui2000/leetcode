# Running Sum 1D array - O(n) run-time
def runningSum(nums):
    if (len(nums) == 0):
        return []
    ans = [nums[0]]
    for pos in range(1, len(nums)):
        ans.append(ans[pos-1]+nums[pos])
    return ans
    # Alternative using the accumulate function in python
    # import operator
    # from itertools import accumulate
    # return list(accumulate(nums))

nums = [1,2,3,4]
assert runningSum(nums) == [1,3,6,10]
nums = [1,1,1,1,1]
assert runningSum(nums) == [1,2,3,4,5]
nums = [3,1,2,10,1]
assert runningSum(nums) == [3,4,6,16,17]