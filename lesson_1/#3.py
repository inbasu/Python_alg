def line_f(a, b):
    #a:(x1,y1) b:(x2,y2)
    k = (a[1]-b[1])/(a[0]-b[0])
    b = a[1] - k*a[0]
    if b > 0:
        b = f'+{b}'
    elif b == 0:
        b = ''    
    return f'y = {k}*x{b}'
    

if __name__ == '__main__':
    a, b = [0,1],[5,5]
    print(line_f(a, b))
    a, b = [-4,1],[5,5]
    print(line_f(a, b))
    a, b = [4,1],[5,5]
    print(line_f(a, b))
    a, b = [1,0],[0,1]
    print(line_f(a, b))
