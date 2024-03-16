import datetime

# zad2
x = 1
y = 2

print('Dodawanie: ',  x + y)
print('Odejmowanie: ', x - y)
print('Mnożenie: ', x * y)
print('Dzielenie', x / y)

# # zad3
# print('Podaj swoje imię: ')
# name = input();
# print('Witaj ', name)
#
# # zad4
# lnght = int(input("Ile liczb chcesz podać ?"))
# sum = 0
# for i in range(lnght):
#     i = int(input("Podaj liczbe: "))
#     sum += i
#
# print("Suma wynosi: ", float(sum))
#
# # zad5
# print(sum(range(8, 81)))
#
# # zad6
# x = datetime.date.today()
# print(x)
#
# rok = int(input("podaj rok"))
# miesiac = int(input("podaj miesiac"))
# dzien = int(input("podaj dzien"))
# date = datetime.date(rok, miesiac, dzien)
#
# print(x - date)
#
# # zad7
# def dodawanie(x, y):
#     return x + y
#
# def odejmowanie(x, y):
#     return x - y
#
# def mnozenie(x, y):
#     return x * y
#
# def dzielenie(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Nie można dzielić przez zero."
#
# print("Wybierz operację:")
# print("1. Dodawanie")
# print("2. Odejmowanie")
# print("3. Mnożenie")
# print("4. Dzielenie")
#
# wybor = input("Podaj numer operacji (1/2/3/4): ")
#
# if wybor not in ('1', '2', '3', '4'):
#     print("Nieprawidłowy wybór.")
# else:
#     liczba1 = float(input("Podaj pierwszą liczbę: "))
#     liczba2 = float(input("Podaj drugą liczbę: "))
#
#     if wybor == '1':
#         print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))
#     elif wybor == '2':
#         print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))
#     elif wybor == '3':
#         print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))
#     elif wybor == '4':
#         wynik_dzielenia = dzielenie(liczba1, liczba2)
#         print(liczba1, "/", liczba2, "=", wynik_dzielenia)
