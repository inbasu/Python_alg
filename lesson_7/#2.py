import random


def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result



def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mindle = len(arr)//2
    return merge(merge_sort(arr[:mindle]),merge_sort(arr[mindle:]))

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(20)]
    print(f'presort: {arr}\npostsort:{merge_sort(arr)}')
