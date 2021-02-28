# 1770. Maximum Score from Performing Multiplication Operations



# Recursive helper method to determine to pick start or end of the array
# to use for computation
# return 0 = start, 1 = end => First attempt
# def helper(nums, multipliers, start, end, m_pos):
#     if (m_pos == len(multipliers)-1):
#         return max(multipliers[m_pos]*nums[start], multipliers[m_pos]*nums[end])
#     if (multipliers[m_pos] * nums[start] > multipliers[m_pos] * nums[end]):
#         return 0
#     elif (multipliers[m_pos] * nums[start] < multipliers[m_pos] * nums[end]):
#         return 1
#     else:
#         return helper(nums, multipliers, start + 1, end - 1, m_pos)


# def maximumScore(nums, multipliers):
#     ans = 0
#     start = 0
#     end = len(nums)-1
#     for i in range(0, len(multipliers)):
#         print(ans)
#         if ((multipliers[i] * nums[start]) > (multipliers[i] * nums[end])):
#             print("first if statement")
#             print(f"multipliers[i] * nums[start] = {multipliers[i] * nums[start]}")
#             print(f"multipliers[i] * nums[end] = {multipliers[i] * nums[end]}")
#             ans += (multipliers[i] * nums[start])
#             start += 1
#         elif ((multipliers[i] * nums[start]) < (multipliers[i] * nums[end])):
#             print("second if statement")
#             print(f"multipliers[i] * nums[start] = {multipliers[i] * nums[start]}")
#             print(f"multipliers[i] * nums[end] = {multipliers[i] * nums[end]}")
#             ans += (multipliers[i] * nums[end])
#             end -= 1
#         else:
#             print("third if statement")
#             print(f"multipliers[i] * nums[start] = {multipliers[i] * nums[start]}")
#             print(f"multipliers[i] * nums[end] = {multipliers[i] * nums[end]}")
#             which = helper(nums,multipliers,start+1, end-1,i)
#             if (which == 0):
#                 ans += (multipliers[i] * nums[start])
#                 start += 1
#             else:
#                 ans += (multipliers[i] * nums[end])
#                 end -= 1

#     return ans

# nums = [-5,-3,-3,-2,7,1]
# multipliers = [-10,-5,3,4,6]

# print(maximumScore(nums, multipliers))


# After help
def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    @lru_cache(2000) 
    def dfs(l,r,i):
        if (i == len(multipliers)):
            return 0
        return max((nums[l]*multipliers[i] + dfs(l+1, r, i+1)),(nums[r]*multipliers[i] + dfs(l, r-1, i+1)))
    
    return dfs(0,len(nums)-1,0)