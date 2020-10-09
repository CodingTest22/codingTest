def solution(array, commands):
    answer = []
    for x, y, z in commands:
        arr = array[x-1:y]
        arr.sort()
        answer.append(arr[z-1])
    return answer

arrays = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arrays, command))
