import random

def buble(arr):
    lenght = len(arr)
    for _ in range(lenght):
        for i in range(lenght-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(20)]
    print(f'presort: {arr}\npostsort:{buble(arr)}')
