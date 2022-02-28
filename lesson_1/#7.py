def triangle(a,b,c):
    if  a + b + c - max(a,b,c) < max(a,b,c):
        return 'Не треугольник'
    elif a == b and b == c:
        return 'Равносторонний'
    elif a == b or a == c or b == c:
        return 'Равнобедренный'
    return 'Разностронний'

if __name__ == '__main__':
    print(triangle(6,6,6))
    print(triangle(6,6,2))
    print(triangle(4,5,6))
    print(triangle(7,2,3))
