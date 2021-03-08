# 5. Longest Palindromic Substring

# Brute Force Algorithm first to expand at every point
def expandAroundCenter(s, mid_point):
    l, r, pos_moved, stringA = mid_point - 1, mid_point+1, False, ""
    while(l >= 0 and r <= len(s)-1):
        if (s[l] == s[r]):
            l -= 1
            r += 1
            pos_moved = True
        else:
            break
    if (not pos_moved):
        stringA = s[mid_point]
    else:
        stringA = s[l+1:r]

    l2, r2, pos_moved2, stringB = mid_point, mid_point+1, False, ""
    while(l2 >= 0 and r2 <= len(s)-1):
        if (s[l2] == s[r2]):
            l2 -= 1
            r2 += 1
            pos_moved2 = True
        else:
            break
    if (not pos_moved):
        stringB = s[mid_point]
    else:
        stringB = s[l2+1:r2]

    l3, r3, pos_moved3, stringC = mid_point-1, mid_point, False, ""
    while(l3 >= 0 and r3 <= len(s)-1):
        if (s[l3] == s[r3]):
            l3 -= 1
            r3 += 1
            pos_moved3 = True
        else:
            break
    if (not pos_moved3):
        stringC = s[mid_point]
    else:
        stringC = s[l3+1:r3]

    max_length = max(len(stringA),max(len(stringB),len(stringC)))
    if (len(stringA) == max_length):
        return stringA
    elif (len(stringB) == max_length):
        return stringB
    else:
        return stringC

def longestPalindrome(s):
    ans = ""
    for i in range(0,len(s)):
        crnt = expandAroundCenter(s,i)
        if (len(crnt) >= len(ans)):
            # print(f"Length of current: {len(crnt)} and crnt = {crnt} while length of ans is {len(ans)} and ans = {ans}")
            ans = crnt
    return ans

s = "abab"
print(longestPalindrome(s))
        