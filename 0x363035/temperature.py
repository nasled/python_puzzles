


def solution (T):
    indexes = []

    for t in T:
        for j_key, j_value in enumerate(T):
            if j_value > t:
                indexes.append(j_key)
            break

    # print(indexes)
    sorted_indexes = sorted(indexes)
    return sorted_indexes[0]

seq = [5,-2,3,8,6]
seq = [-5,-5,-5,-42,6,12]


print(solution(seq))