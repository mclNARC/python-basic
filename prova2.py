"""


def main():
    year = int(input("Digite um ano: "))
    if(year == 1918):
        print("26/09/1918")
    if(year == 1700 or year == 1800 or year == 1900):
        print(f"12/09/{year}")
    if(year % 400 == 0):
        print(f"12/09/{year}")
    if(year % 4 == 0):
        if(year % 100 == 0):
            print(f"13/09/{year}")
        else:
            print(f"12/09/{year}")
    else:
        print(f"13/09/{year}")
main()


"""


def chooseone_day(year):
    if year == 1918:
        asw = '26.09.1918'
    elif ((year <= 1917) and (year % 4 == 0)) or ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        asw = '12.09.{}'.format(year)
    else:
        asw = '13.09.{}'.format(year)

    return asw


if __name__ == '__main__':
    year = int(input('Ano: ').strip())

    print(f'Resultado: {chooseone_day(year)}')