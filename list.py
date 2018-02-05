def numbers_in_lists(s):
    # YOUR CODE
    list = []
    i = 1
    max = int(s[0])
    list.append(max)
    sublist = []
    while i < len(s):
        if int(string[i]) > max:
            list.append(int(s[i]))
            max = int(int(s[i]))
            i += 1
        else:
            while i < len(s) and int(s[i]) <= max:
                sublist.append(int(s[i]))
                i += 1
            list.append(sublist)
            sublist = []
    return list

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print(numbers_in_lists(string))