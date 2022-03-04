from math import sqrt
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
def prime(i):
    # мы проходим все не четные числа и определяем их "простоту" деля эти числа на нечетные делители
    # в диапозоне от 3 до квадратного корня из этого числа.
    # сложность для каждой проверки sqrt(n)/2 всего мы делаем и всего проверяем n/2 чисел
    # сложность n*sqrt(n)/4
    num = 3
    count = 2
    while True:
        condi = True
        if count >= i:
            break
        num += 2
        for div in range(3,int(sqrt(num)+1),2):
            if not num % div:
                condi = False
                break
        if condi:
             count += 1
        # print(num, count)
    return num


def eratosfen(idx):
    #Мы проходим ОПРЕДЕЛЕННЫЙ диапазон и в нем ищем все простые числа с помощью решета  Эратосфена,
    # достигнув нужного индекса возвращаем его
    #расширение списка непростых чисел узкое место алгоритма
    # сложность n*ln(ln(n)) *где n диапазон поиска << ВЗЯТО С ВИКИ
    not_prime = [0]
    # primes = [2]
    count = 1
    end = 10_000
    for i in range(2,end):
        if i not in not_prime:
            if count == idx:
                return i
            # primes.append(i)
            count += 1
            not_prime += [j for j in range(i**2, end, i)]
    # print(len(primes))


@time_eff
def test(n):
    return eratosfen(n)



if __name__ == '__main__':
    n = 1_000
    print(prime(n))
    print(test(n))