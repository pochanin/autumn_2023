dnk = input('Введите ДНК: ')
dnk = dnk.replace('G', '1').replace('C', '2').replace('T','3').replace('A','4')
dnk = dnk.replace('1', 'C').replace('2', 'G').replace('3','A').replace('4','T')
print('РНК: ', dnk)