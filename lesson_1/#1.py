def sum_and_mult(num):
    a, b, c = str(num)
    sum = int(a) + int(b) + int(c)
    mult = int(a) * int(b) * int(c)
    return f'Сумма чисел: {sum}\nПроизведение: {mult}'
    

if __name__ == '__main__':
    print(sum_and_mult(666))
    print(sum_and_mult(612))
    print(sum_and_mult(100))
    print(sum_and_mult(123))
