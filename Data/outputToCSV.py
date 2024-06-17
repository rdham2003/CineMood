def convert(lst):
    str = ''
    for i in range(0, len(lst), 2):
        str = str + f'{lst[i]}, '
    return str

outputLst = "1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 1"

if __name__ == '__main__':
    print(convert(outputLst))