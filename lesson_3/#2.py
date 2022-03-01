import random

lst = [random.randint(1,99) for _ in range(15)]

def even(lst):
   return [i for i in range(len(lst)) if lst[i] % 2 == 0]

if __name__ == '__main__':
   print(lst,even(lst))
