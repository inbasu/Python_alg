from collections import deque


HEX =  ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'\
         , '0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E','F'] 


def easy_hex():
    a, b = int(input('first number = '), 16) , int(input('second number = '), 16)
    return f'sum = {hex(a + b)[2:]}, mult = {hex(a * b)[2:]}'    

    
def hex_sum(hex_1, hex_2):
    '''Сложение столбиком'''
    hex = HEX 
    tmp = 0    
    hex_1, hex_2 = deque(hex_1), deque(hex_2)
    result = deque([])
    if len(hex_2) > len(hex_1):
        hex_1, hex_2 = hex_2, hex_1
    for _ in range(len(hex_1) - len(hex_2)):
        hex_2.appendleft('0')
    for _ in range(len(hex_1)):
        idx = hex.index(hex_1.pop()) + hex.index(hex_2.pop())
        result.appendleft(hex[idx+tmp])
        tmp = 0
        if idx > 15:
            tmp = 1
    if tmp:
        result.appendleft(hex[tmp])
    return list(result)

def hex_mult(hex_1, hex_2):
    '''умножение столбиком'''
    hex = HEX 
    hex_1, hex_2 = deque(hex_1), deque(hex_2)
    result = deque([])
    temp_result = [] 
    decimal = 0
    for digit_1 in reversed(hex_1):
        tmp = 0
        one_mults = deque([])
        digit_1 = hex.index(digit_1)
        for digit_2 in reversed(hex_2):
            digit_2 = hex.index(digit_2)
            rst = digit_1 * digit_2
            idx = (rst % 16) + tmp
            one_mults.appendleft(hex[idx])
            tmp = rst // 16
            if idx > 15:
                tmp += 1
        if tmp:
            one_mults.appendleft(hex[tmp])
        for _ in range(decimal):
            one_mults.append('0')
        temp_result.append(one_mults)
        decimal += 1
    for num in temp_result:
        result = hex_sum(result, num)
    return list(result)


if __name__ == '__main__':
    # print(easy_hex())
    print(hex_sum(['A', '2'], ['C','4','F']))
    print(hex_mult(['A', '2'], ['C','4','F']))