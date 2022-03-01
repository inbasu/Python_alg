import random

lst = [random.randint(1,9) for _ in range(15)]

def min_2(lst):
   return lst.pop(lst.index(min(lst))), lst.pop(lst.index(min(lst)))


def min_2_2(lst, val=2):
   result = []
   for _ in range(val):
      mini = min(lst)
      lst.remove(mini)
      result.append(mini)
   return result


if __name__ == '__main__':
   lst2 = lst.copy()
   print(lst)
   print(min_2(lst))
   print(min_2_2(lst2))