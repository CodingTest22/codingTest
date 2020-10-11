def Getcommand(array, command):
    _arr = array[command[0]-1:command[1]]
    _arr.sort()
    print(_arr)
    return _arr[command[2]-1]

def solution(array, commands):
    answer = []
    for idx in commands:
        answer.append(Getcommand(array, idx))
    return answer