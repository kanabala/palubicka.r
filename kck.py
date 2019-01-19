import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag

dane = pd.read_csv(r"C:\Users\jpalu\Desktop\sub1trial10.csv", delimiter=',', engine='python')
sygnal = dane['kolumna2']
wyswietlane=dane['kolumna6']

t = np.linspace(0,37.89,200*37.89)
probkowanie=200
czestOdciecia1=49
czestOdciecia2=51
przefiltrowany = ag.pasmowozaporowy(sygnal, probkowanie, czestOdciecia1,czestOdciecia2)

przepust1=1
przepust2=50
przepuszczony=ag.pasmowoprzepustowy(sygnal,probkowanie,przepust1,przepust2)

#filtracja sygnału- filtry: pasmowozaporowy i pasmowoprzepustowy
'''plt.subplot(3,1,1)
plt.plot(t,sygnal)
plt.title("Sygnał dla danych sub1trial10")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.subplot(3,1,2)
plt.plot(t,przefiltrowany)
plt.title("Sygnał po zastosowaniu filtra pasmowozaporowego")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.subplot(3,1,3)
plt.plot(t,przepuszczony)
plt.title("Sygnał po zastosowaniu filtra pasmowoprzepustowego")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.show()'''

#sygnał i liczby (porównanie) - całość
'''plt.subplot(2,1,1)
plt.plot(t,przepuszczony)
plt.title("Przefiltrowany sygnał sub1trial10")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.subplot(2,1,2)
plt.plot(t,wyswietlane)
plt.title("Wyświetlane cyfry")
plt.xlabel('Czas [s]')
plt.ylabel('Cyfra')
plt.show()'''

#porównanie mrugnięć i wyświetlanych cyfr cz1
'''plt.subplot(2,1,1)
plt.plot(t,przepuszczony)
plt.xlim(0,18)
plt.title("Pierwsza połowa przefiltrowanego sygnału sub1trial10")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.subplot(2,1,2)
plt.plot(t,wyswietlane)
plt.xlim(0,18)
plt.title("Wyświetlane cyfry")
plt.xlabel('Czas [s]')
plt.ylabel('Cyfra')
plt.show()'''

#porównanie mrugnięć i wyświetlanych cyfr cz2
'''plt.subplot(2,1,1)
plt.plot(t,przepuszczony)
plt.xlim(18,38)
plt.title("Druga połowa przefiltrowanego sygnału sub1trial10")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.subplot(2,1,2)
plt.plot(t,wyswietlane)
plt.xlim(18,38)
plt.title("Wyświetlane cyfry")
plt.xlabel('Czas [s]')
plt.ylabel('Cyfra')
plt.show()'''

max=0
info=[]
for i in range(len(przepuszczony)):
    if przepuszczony[i]>0.06:
        max = przepuszczony[i]
        if max < przepuszczony[i+1]:
            max = przepuszczony[i+1]
            info.append(wyswietlane[i])
print(info)
print('Zdekodowana informacja dla sygnału sub1trial10: 3 3 4 1 3 5 2 4 1 3 4 1 3 5')
