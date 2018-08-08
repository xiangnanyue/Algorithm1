def findKlargest(k, A, B):
    lowA = 0
    highA = len(A) - 1
    lowB = 0
    highB = len(B) - 1
    k_rest = k
    while lowA <= highA and lowB <= highB:
        if k_rest == 1:
            return min(A[lowA], B[lowB])
        divide = int(k_rest / 2) - 1    
        midA = int(lowA + divide)
        midA = highA if midA > highA else midA
        midB = int(lowB + divide)
        midB = highB if midB > highB else midB
        
        if A[midA] <= B[midB]:
            lowA = midA + 1
        elif A[midA] > B[midB]:
            lowB = midB + 1
        k_rest = k - lowA - lowB

    if lowA > highA:
        lowB += k_rest
        kflag = B[lowB-1]
    elif lowB > highB:
        lowA += k_rest
        kflag = A[lowA-1]
    return kflag

if __name__ == '__main__':
    #A = [1,2,3,4,5,6]
    A = []
    B = [2,3,4,5]
    for k in range(1, 11):
        result = findKlargest(k, A, B)
        print(k, result)