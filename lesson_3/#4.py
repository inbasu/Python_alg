import random

lst = [random.randint(1,9) for _ in range(15)]
 
def trick(lst):
    lst.sort()
    try:
        if len(lst) == 1 or len(list(set(lst))) == len(lst):
            return lst
        return trick([lst[i] for i in range(len(lst)) if lst[i] == lst[i-1]])
    except RecursionError:
        return 'Рекурсия не тянет'

def max_dup(lst):
    lst.sort()
    max = -999
    count = 0
    max_count = 0
    for i in range(len(lst)):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            if count > max_count:
                max = lst[i-1]
                max_count = max
            count = 0
    return max



if __name__ == '__main__':
    print(lst)
    print(trick(lst))
    print(max_dup(lst))