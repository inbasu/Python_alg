from collections import OrderedDict

def input_ui():
    '''take input in sorted OrderedDict'''
    print('Input company names and quartal incomesplited by " "\nFor stop input use "exit" or empty string:')
    company_dict = {}
    while True:
        data = [i for i in input().split(' ') if i]
        if data == 'exit' or not data:
            return OrderedDict(sorted(company_dict.items(), key = lambda i: i[1]))
        company_dict[data[0]] = sum([int(i) for i in data[1:]])


def avarage(data):
    return sum([num for num in data.values()])/len(data)


def calc():
    data = input_ui()
    avrg = avarage(data)
    print(f'Avarage year income is {avrg}, \Company with income lowaer than avarage:')
    med = True
    for key, val in data.items():
        if val > avrg and med:
            print('Company with income lowaer than avarage:')
            med = False
        print(key)

    
if __name__ == '__main__':
    calc()
