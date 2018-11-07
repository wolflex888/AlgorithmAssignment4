import time
import sys

def DCCrossSub(lst, low, high, mid):
    # cross section of left piece and right piece #
    lowNow, highNow = 0, 0
    i = mid
    s = 0
    leftsum = lst[i] - 1

    # left index
    while i >= low:
        s = s + lst[i]
        if s > leftsum:
            leftsum = s
            lowNow = i
        i = i-1

    j = mid+1
    s = 0
    rightSum = lst[j] -1


    #right index
    while j <=high:
        s = s+lst[j]
        if s > rightSum:
            rightSum = s
            highNow = j
        j = j+1
    return (lowNow, highNow, leftsum+rightSum)

def DC(lst, low, high):
    # divide and conquer #
    if low == high:
        return (low, high, lst[low])
    mid = (low+high)//2
    llow, lhigh, leftsum = DC(lst, low, mid)
    rlow, rhigh, rightsum = DC(lst, mid+1, high)
    clow, chigh, crossum = DCCrossSub(lst, low, high, mid)
    if leftsum >= rightsum and leftsum >= crossum:
        # flag = "left"
        return llow, lhigh, leftsum
    elif rightsum >= leftsum and rightsum >= crossum:
        # flag = "right"
        return rlow, rhigh, rightsum
    else:
        # flag = "cross"
        return clow, chigh, crossum

def DP(lst):
    # dynamic programing piece #
    # find the two index first then calculate sum #
    matrix = [0 for i in range(len(lst))]
    start = len(lst) - 1
    end = 0
    matrix[0] = lst[0]
    for i in range(1, len(lst)):
        matrix[i] = max(lst[i], matrix[i-1]+lst[i])
        if (matrix[end] < matrix[i]):
            end = i
    # print(matrix)
    matrix = [0 for j in range(len(lst))]
    matrix[len(lst) - 1] = lst[len(lst) - 1]
    # print(matrix)
    for j in range( len(lst) - 2, -1, -1 ):
        matrix[j] = max(lst[j], matrix[j + 1] + lst[j])
        if matrix[start] < matrix[j]:
            # print("entered %d"%j)
            start = j

    if end <= start:
        # print(end, start)
        # print("bing")
        return None
    # print(end, start)
    return start, end, sum(lst[start:end+1])

def main():
    
    # check input #
    if len(sys.argv) < 4:
        print("error: insufficient number of argument")
        exit(1)
    # read file #
    inputFile = sys.argv[1]
    choice = sys.argv[2]
    outputFile = sys.argv[3]
    totalTime = 0
    with open(inputFile, "r") as inp:
        with open(outputFile, "w") as out:
            numLine = inp.readline()
            for line in inp:
                tmp = line.split(",")
                tmp = list(map(float, tmp))
                # read algorithm #
                if choice == "DC":
                    # do the calculation each line of input #
                    start = time.time()
                    rawResult = DC(tmp, 0, len(tmp)-1)
                    runTime = round((time.time()-start) * 1000, 2)
                    totalTime+=runTime
                    result = str(round(rawResult[2], 2)) + "," + str(rawResult[0]+1) + "," + str(rawResult[1]+1) + "," + str(runTime) + "\n"
                    out.write(result)
                
                elif choice == "DP":
                    # do the calculation each line of input #
                    start = time.time()
                    rawResult = DP(tmp)
                    runTime = round((time.time()-start) * 1000, 2)
                    totalTime += runTime
                    result = str(round(rawResult[2], 2)) + "," + str(rawResult[0]+1) + "," + str(rawResult[1]+1) + "," + str(runTime) + "\n"
                    out.write(result)
    # for total time analysis #
    print("The executing time is %f"%totalTime)



if __name__ == "__main__":
    main()