def minOperations(boxes):
    if (len(boxes) == 0):
        return []
    ans = []
    for i in range(len(boxes)):
        numToMove = 0
        for j in range(len(boxes)):
            if (i == j or boxes[j] == '0'):
                continue
            numToMove += abs(i - j)
        ans.append(numToMove)
    return ans

print(minOperations('110'))
print(minOperations('001011'))
                


        