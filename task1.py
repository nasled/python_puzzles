
# unique chars
def algo11(string):
    dict = {}
    for char in string:
        if char in dict.keys():
            return False
        
        dict[char] = True 
    return True
        
# print(algo11('asdf'))
# print(algo11('asdfa'))


# permutation
def algo12(string1, string2):
    if len(string1) != len(string2):
        return False
    
    dict = {}
    for char1 in string1:
        if char1 in dict.keys():
            dict[char1] = dict[char1] + 1
        else:
            dict[char1] = 1
            
    for char2 in string2:
        if char2 not in dict.keys() or dict[char2] == 0:
            return False
        else:
            dict[char2] = dict[char2] - 1
            
    return True
    
# print(algo12('asdfga', 'agfdsa'))
# print(algo12('agfdsa', 'asdfgaa'))
# print(algo12('aggffddsa', 'asddffgga'))
# print(algo12('aggffddsa', 'asddffgaa'))


# replace space to %20 in string
def algo13(string):
    new_string = ''
    for char in string:
        if char == ' ':
            new_string += '%20'
        else:
            new_string += char
    return new_string

# print(algo13('a b c d e'))


# palindrome
def algo14(string):
    new_string = ''
    for char in reversed(string):
        new_string += char

    return True if new_string == string else False

# print(algo14('123454321'))
# print(algo14('1234556789'))


# only 1 diff between strings
def algo15(string1, string2):
    missmatch_found = False

    longest = string1 if len(string1) >= len(string2) else string2
    smallest = string2 if longest == string1 else string1

    index1 = 0
    index2 = 0

    while(len(longest) > index1 and len(smallest) > index2):
        if longest[index1] != smallest[index2]:
            if missmatch_found == True:
                return False
            else:
                missmatch_found = True

            # offset longer string on replacement
            if len(longest) != len(smallest):
                index2 = index2 + 1

        index1 = index1 + 1
        index2 = index2 + 1

    return True

# print(algo15('pale', 'ple'))
# print(algo15('pales', 'pale'))
# print(algo15('pale', 'bale'))
# print(algo15('pale', 'bake'))


# pack the string
def algo16(string):
    dict = {}
    for char in string:
        if char in dict.keys():
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1

    new_string = ''
    for key in dict:
        new_string = new_string + key + str(dict[key])

    return new_string

# print(algo16('abbcccddddeeeeeaaaa'))


# move NxN matrix on 90o degress
def algo17(matrix):
    converted_matrix = [x[:] for x in matrix]
    length = len(matrix[0])

    for i in range(length):
        for j in range(length):
            k = length - i - 1
            l = j
            converted_matrix[l][k] = matrix[i][j]

    return converted_matrix

# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# print(algo17([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]))

# [[41, 31, 21, 11], [42, 32, 22, 12], [43, 33, 23, 13], [44, 34, 24, 14]]
# print(algo17([
#     [11, 12, 13, 14],
#     [21, 22, 23, 24],
#     [31, 32, 33, 34],
#     [41, 42, 43, 44]
# ]))


# set row and line to 0 for 0 elemement in MxN matrix
def algo18(matrix):
    zero_lines = []
    zero_rows = []

    line_length = len(matrix)
    rows_length = len(matrix[0])

    for i in range(line_length):
        for j in range(rows_length):
            if matrix[i][j] == 0:
                zero_lines.append(i)
                zero_rows.append(j)

    for i in range(line_length):
        for j in range(rows_length):
            for k in zero_lines:
                if i == k:
                    matrix[i][j] = 0

            for k in zero_rows:
                if j == k:
                    matrix[i][j] = 0

    return matrix

# print(algo18([
#     [1,2,3],
#     [4,0,6],
#     [7,8,9],
#     [0,12,13]
# ]))


def is_substring(string_haystack, string_needle):
    return string_needle in string_haystack


def algo19(string1, string2):
    return is_substring(string1 + string1, string2)

# print(algo19('waterbottle', 'erbottlewat'))
