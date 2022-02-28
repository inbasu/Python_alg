def rec_findall(num, numrow):
    if len(numrow) == 1 and str(num) == numrow[0]:
        return 1
    elif str(num) == numrow[0]:
        count = 1
    else:
        count = 0
    return count + rec_findall(num, numrow[1:])

def findall(num, numrow):
    count = 0
    for digit in numrow:
        if num == int(digit):
             count += 1
    return count

if __name__ == '__main__':
    inp = input()
    print(rec_findall(5, inp))
    print(findall(5, inp))