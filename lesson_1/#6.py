import string

def letters_range(idx):
    letter = string.ascii_lowercase[idx- 1]
    return f'{idx} letter is "{letter}"'
    

if __name__ == '__main__':
    print(letters_range(1))
