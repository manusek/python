# zad10

# def interpolacja_lagrangea(węzły):
#     def wielomian_bazowy(j):
#         def funkcja_bazowa(x):
#             iloczyn = 1
#             for m in range(len(węzły)):
#                 if m != j:
#                     iloczyn *= (x - węzły[m][0]) / (węzły[j][0] - węzły[m][0])
#             return iloczyn
#         return funkcja_bazowa
#
#     def wielomian_lagrangea(x):
#         wynik = 0
#         for j in range(len(węzły)):
#             wynik += węzły[j][1] * wielomian_bazowy(j)(x)
#         return wynik
#
#     return wielomian_lagrangea
#
# # Węzły
# węzły = [(1, 5), (2, 7), (3, 6)]
#
# # Obliczanie funkcji interpolującej
# funkcja_interpolująca = interpolacja_lagrangea(węzły)
#
# # Testowanie interpolacji
# wartości_x = [1.5, 2.5, 3.5]
# for x in wartości_x:
#     print(f"f({x}) = {funkcja_interpolująca(x)}")

#zad11

import numpy as np

def gauss_elimination_with_pivoting(A, b):
    n = len(b)
    A = A.astype(float)  # Zapewnienie działania na liczbach zmiennoprzecinkowych
    b = b.astype(float)

    for i in range(n):
        # Wybór elementu podstawowego
        max_row = np.argmax(abs(A[i:n, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Eliminacja Gaussa
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Wsteczne podstawienie
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

# Dane z zadania
A = np.array([[3, 0, 6],
              [1, 2, 8],
              [4, 5, -2]])

b = np.array([-12, -12, 39])

# Rozwiązanie układu równań
x = gauss_elimination_with_pivoting(A, b)
print("Rozwiązanie x:", x)


#zad12
#bilbioteka do tworzania macierzy i rozwiazywanie uklad liniowych
# import numpy as np
#
# def aproksymacja_wielomianowa(węzły, stopień):
#     n = len(węzły)
#     A = np.zeros((n, stopień + 1))
#     #tworzy macierz zer o podanym rozmiarze
#     b = np.zeros(n)
#
#     for i, (x, y) in enumerate(węzły):
#         for j in range(stopień + 1):
#             A[i][j] = x ** j
#         b[i] = y
#
#     #przechowywanie wspolczynnikow wielomianu ktore sa obliczane metoda najmniejszych kwadratow
#     coeffs = np.linalg.lstsq(A, b, rcond=None)[0]
#
#     def funkcja_aproksymacyjna(x):
#         result = 0
#         for j in range(stopień + 1):
#             result += coeffs[j] * (x ** j)
#         return result
#
#     return funkcja_aproksymacyjna
#
#
# # Węzły aproksymacji
# węzły_aproksymacji = [(0, 4), (3, 5), (6, 4), (9, 1), (12, 2)]
#
# # Stopień wielomianu
# stopień_aproksymacji = 3
#
# # Obliczanie funkcji aproksymacyjnej
# funkcja_aproksymacyjna = aproksymacja_wielomianowa(węzły_aproksymacji, stopień_aproksymacji)
#
# # Testowanie aproksymacji
# wartości_x = [0, 3, 6, 9, 12]
# for x in wartości_x:
#     print(f"f({x}) = {funkcja_aproksymacyjna(x)}")
