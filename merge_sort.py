
def merge(left, right):
    if not len(left):
        return right

    if not len(right):
        return left

    result = []
    i = 0
    j = 0
    while len(left) > i and len(right) > j:

        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

        if len(left) == i:
            for k in right[j:]:
                result.append(k)

        if len(right) == j:
            for k in left[i:]:
                result.append(k)

    return result


def merge_sort(list):
    if len(list) == 0 or len(list) == 1:
        return list

    mid = round(len(list) / 2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

# q = [1,5,2,6,3,7,4,8,9,10,11]
# q = [2,1,3,1,2]
# w = merge_sort(q)
# print(w)