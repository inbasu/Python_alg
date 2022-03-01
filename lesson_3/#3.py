import random

lst = [random.randint(1,99) for _ in range(15)]

def swap_min_max(lst):
    mini = lst.index(min(lst))
    maxi = lst.index(max(lst))
    lst[mini], lst[maxi] = max(lst), min(lst)
    return lst

def bad_swap(lst):
    '''Не понимаю почему так не работает'''
    lst[lst.index(min(lst))], lst[lst.index(max(lst))] = max(lst), min(lst)
    return lst




if __name__ == '__main__':
    lstz = lst.copy()
    print(lst)
    print(swap_min_max(lst))
    print(bad_swap(lstz))
