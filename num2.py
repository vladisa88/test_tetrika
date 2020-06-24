
alphabet = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,

}


def file_work():
    # open file and read data in python list
    # split by ','
    with open('names.txt', 'r') as f:
        names = f.read().split(',')
    f.close()
    # sort
    names.sort()
    # delete '"' symbols
    for i in range(len(names)):
        names[i] = names[i].rstrip('"').lstrip('"')
    # count what we need
    res = 0
    for i in range(len(names)):
        sum = 0
        for j in names[i]:
            sum += alphabet[j]

        res += sum * (i + 1)

    return res
