# 11. Container With Most Water

# Initial solution, worked but too slow
def maxArea_initial(height):
    ans = 0
    for i in range(0, len(height)):
        for j in range(i+1, len(height)):
            # Making sure the height between two rectangles are equal
            ans = max(ans, (j - i) * min(height[i], height[j]))
    return ans
    
# Final attempt
def maxArea(height):
    l, r, ans, h = 0, len(height)-1, 0, 0
    while(l < r):
        area = r - l
        if (height[l] <= height[r]):
            h = height[l]
            l += 1
        else:
            h = height[r]
            r -= 1
        ans = max(ans, h*area)
    return ans
 
height = [2,1,2]
print(maxArea(height))