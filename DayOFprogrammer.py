"""
#questão01
def num_velas_aniversario(cd):
    velas_altura = 0
    mx = max(cd)

    for i in range(0, len(cd)):
        if (cd[i] == mx):
            velas_altura += 1

    return velas_altura


if __name__ == '__main__':

    cd_cont = int(input('Número de velas no bolo: '))

    cd = list(map(int, input('Altura das velas: ').rstrip().split()))

    print(f'Velas mais altas: {num_velas_aniversario(cd)}')
"""
#questão02
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