# First attempt - brute force approach O(N * M) where N is the
# queries length and M is the array length
def sumEvenAfterQueries(A, queries):
    ans = []
    for query_pos in range(0, len(queries)):
        A[queries[query_pos][1]] += queries[query_pos][0]
        toBeAdded = 0
        for ele in A:
            if (ele%2==0):
                toBeAdded += ele
        ans.append(toBeAdded)
    return ans

# Second attempt - more efficient approach. Keep track of the
# sum once
def sumEvenAfterQueries2(A, queries):
    ans = []
    old_sum = 0
    for ele in A:
        if ele%2==0:
            old_sum += ele
    for query_pos in range(0, len(queries)):
        old_val = A[queries[query_pos][1]]
        A[queries[query_pos][1]] += queries[query_pos][0]
        if (A[queries[query_pos][1]] % 2 == 0):
            if (old_val % 2 != 0):
                old_sum += A[queries[query_pos][1]] 
            else:
                old_sum += queries[query_pos][0]
        else:
            old_sum -= old_val
        ans.append(old_sum)
    return ans

print(sumEvenAfterQueries2( [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))
