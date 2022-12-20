'''
******************
Rastgele Fonksiyonunu kullanarak bir taş-kağıt-makas oyunu
******************

Kurallar;
Taş kağıt, kağıt kazanır.
Taş makas, taş kazanır.
taş taş, berabere biter.

kağıt taş, kağıt kazanır.
kağıt makas, makas kazanır.
kağıt kağıt, berabere biter.

makas kağıt, makas kazanır.
makas taş, taş kazanır.
makas makas, berabere biter.

'''
import random
__author__ = 'Mustafa Yalvac <mst-99@outlook.com>'

'''
Genel Karar
'''
youwins = 0
pcwins = 0

i = 0
print('Oyun için 5 hakkınız bulunuyor. ')

'''
Fonksiyonlar
'''

def _you_won():
    print('Sen kazandın. ')
    global youwins
    youwins += 1

def _pc_won():
    print('Bilgisayar kazandı. ')
    global pcwins
    pcwins += 1

def _you_lost():
    print('\nOYUNU KAYBETTİNİZ. ')

def _pc_lost():
    print('\nTEBRİKLER OYUNU KAZANDINIZ. ')

'''
Döngü, kontrol noktası 
'''

while i < 5:
    you = input('\nTaş = 1, Kağıt = 2, Makas = 3, Birini Seçiniz: ')
    if you == '1':
        print('Taş Seçtiniz. ')
    if you == '2':
        print('Kağıt Seçtiniz. ')
    if you == '3':
        print('Makas Seçtiniz. ')
    _secenekler = ['Taş', 'Kağıt', 'Makas']
    pc = random.choice(_secenekler)
    print('Bilgisayarın Seçimi: ', pc)
    if you == '1' and pc == 'Taş' or you == '2' and pc == 'Kağıt' or you == '3' and pc == 'Makas':
        print('Berabere bitti. ')
    elif you == '1' and pc == 'Makas' or you == '2' and pc == 'Taş' or you == '3' and pc == 'Kağıt':
        _you_won()
    elif you == '1' and pc == 'Kağıt' or you == '2' and pc == 'Makas' or you == '3' and pc == 'Taş':
        _pc_won()
    else:
        print('Geçersiz Seçenek...')
        print('Otomatik olarak Bilgisayar Kazandı. ')
        _pc_won()
    i += 1
'''
Sonuç
'''
print('\nBilgisayar Kazandı. ', pcwins, 'Kere')
print('\nSen Kazandın. ', youwins, 'Kere')

'''
Sonuç
'''
if youwins > pcwins:
    _pc_lost()
elif pcwins > youwins:
    _you_lost()


