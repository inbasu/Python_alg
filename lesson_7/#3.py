import random

def med(arr):
    for _ in range(len(arr)//2):
        arr.remove(min(arr))
        arr.remove(max(arr))
    return arr[0]


def sorted_med(arr):
    return sorted(arr)[len(arr)//2]


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(3)]
    print(f'array: {arr}\nmediant v1: {med(arr)}\nmediant v2: {sorted_med(arr)}')
