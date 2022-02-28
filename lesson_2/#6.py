import random

def check(num, guess):
   if num == guess:
      return True
   if num > guess:
      print(f'Меньше чем {num}')
   else:
      print(f'Больше чем {num}')
   return False


def guess(count = 10):
   num_g = random.randint(0,100)
   for count in range(1,11):
      num = int(input(f'Попытка #{count} из 10: '))
      if check(num, num_g):
         return f'Верно, загаданное число {num}'
   return 'GAME OVER'

      
if __name__ == '__main__':
    print(guess())