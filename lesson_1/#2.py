def logic(a, b, explanation=False):
    left = a << 2
    right = a >> 2
    if explanation:
        print(f'{a} в битах: {bin(a)}.\n\сдвиг влево на 2\
        добавляет два 0 сврава и приводит число к виду {bin(left)},\
        сдвиг вправо удаляет два правых знака => {bin(right)}')
    a_and_b = a & b
    a_or_b = a | b
    a_xor_b = a ^ b
    return left, right, a_and_b, a_or_b, a_xor_b


if __name__ == '__main__':
    print(logic(5, 6))
