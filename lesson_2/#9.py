def sumz(lst:list):
   mx = [0, 0]
   for num in lst:
      # print(num)
      if (summ := sum([int(i) for i in num])) > mx[1]:
         mx = [num, summ]
   return f'num: {mx[0]}\tsumm: {mx[1]}'


def c_sumz(lst:list):
   maxm = [0, 0]
   for num in lst:
      suma = 0
      for dig in num:
         suma += int(dig)
      if suma >= maxm[1]:
         maxm = [num, suma]
   return f'num: {maxm[0]}\tsumm: {maxm[1]}'


def merg_max_sum(lst):
   if len(lst) <= 1:
      res = sum([int(i) for i in lst[0]])
      # print(res, lst)
      return res
   mid = int(len(lst) / 2)
   #print(lst[:mid], lst[mid:]) 
   return merg_max_sum(lst[:mid]) if \
      merg_max_sum(lst[:mid]) > merg_max_sum(lst[mid:]) else \
         merg_max_sum(lst[mid:])



if __name__ == '__main__':
   row = input().split(' ')
   print(sumz(row))
   print(c_sumz(row))
   print(merg_max_sum(row))
