'''Если чесно я не понял задания'''


def func():
    return  {key: [i for i in range(2,10) if key % i == 0]  for key in range(2,100)}

def func_2(start = 2, end = 100):
    result = []
    for i in range(start,end):
        for j in range(2,10):
            check = True
            if i % j:
                check = False
                break
        if check:
            result.append(i)
    return f"в диапозоне[ {start}; {end} ]кратных числам от 2 до 9 :{len(result)} чисел"

def func_2p5(start = 2, end = 100):
    fin = 9
    result = set([i for i in range(start,end)])
    for d in range((fin+1)//2, fin+1):
        result = result & set([i for i in range(0,end, d)])
    return result


def func_3():
    #кратны каждому из чисел в диапазоне от 2 до 9
    div = 9 * 8 * 7 * 5
    #print(func_2(start = 2, end = div +1))
    return f'Каждому из чисел в диапазоне от 2 до 9 кратно {div}'


if __name__ == '__main__':
    print(func())
    print(func_2())
    print(func_3())
