def solution(n, lost, reserve):
    num = 0
    tmpArr = lost
    lost = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(tmpArr))
    print("lost : ", lost)
    print("reserve : ", reserve)
    for idx in lost:
        if(idx-1 in reserve and idx-1 not in lost):
            reserve[reserve.index(idx-1)] = -1
            num = num + 1
            print(idx, ": T")
        elif(idx+1 in reserve and idx+1 not in lost):
            reserve[reserve.index(idx+1)] = -1
            num = num + 1
            print(idx, ": F")
    return n - len(lost) + num