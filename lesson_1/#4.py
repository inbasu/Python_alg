import random

def rand_char(a, b):
    if type(a+b) is str:
        list = [chr(i) for i in range(ord(a),ord(b)+1)]
        return random.choice(list)
    elif type(a+b) is int:
        return random.randint(a, b)
    return random.uniform(a, b)
    

if __name__ == '__main__':
    print(rand_char('a', 'z'))
    print(rand_char(4, 88))
    print(rand_char(1, 8.6))
