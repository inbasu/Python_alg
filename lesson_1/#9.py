import statistics

def mean_mun(a,b,c):
    return statistics.median([a,b,c])


if __name__ == '__main__':
    print(mean_mun(5,7,20))
