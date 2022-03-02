import random


lst = [random.randint(-99,99) for _ in range(15)]

def min_neg(lst):
    elem = - min([abs(i) for i in lst if i <0])
    return f'Максимальный отрицательный элемент {elem} \nего индекс {lst.index(elem)}'

if __name__ == '__main__':
    print(lst)
    print(min_neg(lst))