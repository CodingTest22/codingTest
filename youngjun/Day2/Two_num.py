def solution(a, b):
    answer = 0
    c = 0
    if(a > b):
        c = a
        a = b
        b = c
    for x in range(a,b+1):
        answer += x
    
    return answer

a_1,b_1 = 3, 5
a_2,b_2 = 3, 3
a_3, b_3 = 5, 3

print(solution(a_1, b_1))
print(solution(a_2, b_2))
print(solution(a_3, b_3))
