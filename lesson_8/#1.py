import hashlib


def comp(string):
    h_string = hashlib.sha1(string.encode('utf-8')).hexdigest()
    h_dif_string = []
    for i in range(len(string)):
        for j in range(len(string)):
            if i+j > len(string):
                break
            h_sub = hashlib.sha1(string[i:i+j].encode('utf-8')).hexdigest()
            h_dif_string.append(h_sub)

    # print(f'Hash  {h_string}; подстрок  {len(h_dif_string)}')
    return len(set(h_dif_string))


if __name__ == '__main__':
    s1 = 'alice in wonderland'
    print(comp(s1))
