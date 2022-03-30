from sys import getsizeof as size
#from memory_profiler import profile #https://pypi.org/project/memory-profiler/


#@profile
def sum_som(n:int):
    size_of = 0
    result = 0
    size_of += size(result) + size(n)
    for i in range(n+1): # Цикл с пространственной сложностью O(n)
        result += 1/(-2)**i
        size_of += size(result) + size(i)
    print(size_of)
    return result


#@profile
def geo_sum(n):
    # Рассчет суммы геометрической прогрессии сложность O(1)
    result = (1/(-2)**n * (-0.5) - 1) / (-0.5 - 1)
    print(size(result) + size(n))
    return result



if __name__ == '__main__':
    print(sum_som(50_000))
    print(geo_sum(50_000))