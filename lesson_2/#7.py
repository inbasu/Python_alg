import random


def summ(num):
   if num == 0:
      return 0
   return num + summ(num-1)


def sum(num):
   return num * (num+1) / 2


def check(tests):
   for _  in range(tests):
      i = random.randint(1, 9_00)
      # print(f'{summ(i)} ... {sum(i)}')
      if not summ(i) == sum(i):
         return 'test failed'
   return 'Test sucsess'



if __name__ == '__main__':
   print(check(100))

