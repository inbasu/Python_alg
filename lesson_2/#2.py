def odd_even(num:str):
    odd, even = 0, 0    
    for digit in num:
        if int(digit) % 2:
            even += 1
        else:
            odd += 1
    return odd, even    
    

if __name__ == '__main__':
    print(odd_even('34560'))