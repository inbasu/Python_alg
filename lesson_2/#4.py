def sum_som(n:int):
   result = 0
   for i in range(n+1):
      result += 1/(-2)**i
   return result


def rec_sum(n:int):
   if n == 0:
      return 1
   return 1/(-2)**n + rec_sum(n-1)


def s_sum(n:int):
   return sum([1/(-2)**i for i in range(n+1)])     
   

if __name__ == '__main__':
   for n in range(3):
      print(sum_som(n), s_sum(n), rec_sum(n))
