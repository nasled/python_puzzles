
input = [3, 0, 0, 1, 0, 0]

def solution(A):
    if len(A) > 21:
        raise Exception('Wrong Input')

    # test
    result = 0
    for i in A:

        if i not in [0,1]:
            raise Exception('Wrong Input')

        if i == 1:
            result = result + 1

    return result

print(solution(input))
