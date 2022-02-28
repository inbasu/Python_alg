import string

def letters_range(l1, l2):
    l1_idx = string.ascii_lowercase.index(l1) + 1
    l2_idx = string.ascii_lowercase.index(l2) + 1
    if l1_idx == l2_idx:
        letter_range = 0
    else:
        letter_range = abs(l1_idx - l2_idx) - 1
    return f'{l1} index {l1_idx}, {l2} index {l2_idx}, range: {letter_range}'
    

if __name__ == '__main__':
    print(letters_range('a','b'))
