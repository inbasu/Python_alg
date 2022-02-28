def year(year):
    if not year % 400 or (not year % 4 and year % 100):
        return 'Високосный'
    return 'Не високосный'

if __name__ == '__main__':
    print(year(2020))
    print(year(2021))
    print(year(1990))
    print(year(2020))
