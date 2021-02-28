arr = {1,3,4,0,4,3,1}
input(arr)
output(sum)


def answer(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        sum_ans = -9999999 
        sum_arr = 0
        for i in range(0,len(arr)):
            sum_arr += arr[i]
        crnt_prefix = 0
        for i in range(0, len(arr)):
            crnt_prefix += arr[i]
            sum_suffix = sum_arr - crnt_prefix + arr[i]
            if (crnt_prefix == sum_suffix and crnt_prefix > sum_ans):
                sum_ans = crnt_prefix
    return sum_ans

    # O(n^2)
            



