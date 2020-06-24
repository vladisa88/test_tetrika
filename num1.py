def search_pairs(array: list, sum: int) -> list:
    check_dict = {}  # dict with keys as elements of array
    result = []
    for i in array:
        # add elements of array as dict's keys
        if i in check_dict:
            check_dict[i] += 1
        else:
            check_dict[i] = 1

    for j in check_dict:
        # looking for keys which completes current key to sum
        # and check for repeat
        if (sum - j in check_dict and sum - j > j):
            result.append((j, sum - j))
    return result


arr = [1, 2, 6, 5, 3, 4, 7, 8, 3, 2, -1]
print(search_pairs(arr, 5))
