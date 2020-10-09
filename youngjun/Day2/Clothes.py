def solution(n, lost, reserve):
    answer = n - len(lost)
    for x in reserve:
        for g in lost:
            if x -1 == g:
                answer +=1
                lost.remove(g)
            elif x+1 == g:
                answer +=1
                lost.remove(g)
    return answer

n_1, lost_1, reserve_1 = 5, [2, 4], [1, 3, 5]
n_2, lost_2, reserve_2 = 5, [2, 4], [3]
n_3, lost_3, reserve_3 = 3, [3], [1]

print(solution(n_1, lost_1, reserve_1))
print(solution(n_2, lost_2, reserve_2))
print(solution(n_3, lost_3, reserve_3))
