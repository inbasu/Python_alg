import random

lst = [random.randint(1,999) for _ in range(15)]

def slice_sum(lst):
   slice = sorted([lst.index(min(lst)), lst.index(max(lst))])
   return sum(lst[slice[0]+1: slice[1]])


if __name__ == '__main__':
   print(lst)
   print(slice_sum(lst))
