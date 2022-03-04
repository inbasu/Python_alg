import time

def time_eff(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        t = time.time() - start
        print(f'Time: {t}')
        return res
    return wrapper


@time_eff
def sum_som(n:int):
    # мы проходим все члены последовательности до n-ого и складываем их между собой
    # сложность О(n)
   result = 0
   for i in range(n+1):
      result += 1/(-2)**i
   return result


@time_eff
def geo_sum(n):
    #Константная сложность т.к. мы находим последнее значение последовательности и 
    #подставляем его в формулу сммы членов геометрической последоавтельности 
    # сложность О(1)
    result = (1/(-2)**n * (-0.5) - 1) / (-0.5 - 1)
    return result



if __name__ == '__main__':
    print(sum_som(50_000))
    print(geo_sum(50_000))