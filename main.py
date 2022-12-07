from modul import print_line
import time
from pyfiglet import Figlet

f = Figlet()
print(f.renderText('Finnance Budgeting'))
print('Bisa untuk semua mata uang')
while True:
    budget = int(input('Masukkan pemasukan anda: '))
    if budget < 0:
        print('Pemasukan anda tidak boleh negatif')
        continue
    elif budget == 0:
        print('Pemasukan anda tidak boleh 0')
        continue
    else:
        break

while True:
    choose = input('Apakah anda sudah menikah? (y/n) ').lower()
    if (choose == 'y'):
        # default budgeting percentage (married)
        living = 0.30
        playing = 0.15
        saving = 0.55

    elif (choose == 'n'):
        # default budgeting percentage (single)
        living = 0.30
        playing = 0.20
        saving = 0.50

    else:
        print('Input yang anda masukkan salah')
        continue
    # tiap tiap kategorinya
    percent_living = living * 100
    percent_playing = playing * 100
    percent_saving = saving * 100
    percentage = [percent_playing, percent_living, percent_saving]
    loading = ['20', '45', '67', '87', '100']
    percent_budget = (living + playing + saving) * 100

    budget_living = budget * living
    budget_playing = budget * playing
    budget_saving = budget * saving

    print('========================================================')
    for x in loading:
        if x == '100':
            assign = '(DONE)'
        else:
            assign = '(CHECKING)'
        line_new = '%-12s  %-12s  %-12s' % (
            'Loading.....', str(x)+'%', assign)
        print(line_new)
        time.sleep(0.5)

    print_line('Budget anda', '{:,.3f}'.format(budget))
    print_line('kebutuhan', '{:,.3f}'.format(budget_living))
    print_line('kegiatan', '{:,.3f}'.format(budget_playing))
    print_line('tabungan', '{:,.3f}'.format(budget_saving))
    print('========================================================')
    break
