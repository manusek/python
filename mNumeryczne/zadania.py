# zad1
def horner_scheme(coefficients, x):
    n = len(coefficients)
    result = coefficients[0]

    for i in range(1, n):
        result = result * x + coefficients[i]

    return result

# Przykładowe współczynniki wielomianu: 2x^3 + 3x^2 - 6x + 1
coefficients = [2, 3, -6, 1]

# Punkt, w którym chcemy obliczyć wartość wielomianu
point = float(input("Podaj punkt, w którym chcesz obliczyć wartość wielomianu: "))

# Wywołanie funkcji i wyświetlenie wyniku
result = horner_scheme(coefficients, point)
print(f"Wartość wielomianu w punkcie {point} wynosi: {result}")

# zad2
def horner_scheme(coefficients, x):
    n = len(coefficients)
    result = coefficients[0]

    for i in range(1, n):
        result = result * x + coefficients[i]

    return result

def divide_polynomial_by_binomial(polynomial_coefficients, binomial_root):
    n = len(polynomial_coefficients) - 1  # Stopień wielomianu
    quotient_coefficients = [0] * n
    remainder = 0

    for i in range(n, 0, -1):
        quotient_coefficients[i - 1] = (polynomial_coefficients[i] + remainder) / binomial_root
        remainder = (polynomial_coefficients[i] + remainder) % binomial_root

    return quotient_coefficients, remainder

# Przykładowe współczynniki wielomianu: 2x^3 + 3x^2 - 6x + 1
polynomial_coefficients = [2, 3, -6, 1]

# Dwumian (x - r), gdzie r to pierwiastek dwumianu
binomial_root = float(input("Podaj pierwiastek dwumianu (r): "))

# Wywołanie funkcji i wyświetlenie wyniku
quotient, remainder = divide_polynomial_by_binomial(polynomial_coefficients, binomial_root)

print(f"Wynik dzielenia wielomianu przez dwumian (x - {binomial_root}):")
print(f"Reszta: {remainder}")
print(f"Współczynniki ilorazu: {quotient}")

# zad3
def funkcja(x):
    return x**3 + x - 1

def metoda_bisekcji(funkcja, a, b, dokladnosc):
    if funkcja(a) * funkcja(b) > 0:
        print("Błąd: Funkcja nie spełnia warunków bisekcji w danym przedziale.")
        return None

    iteracja = 0
    while (b - a) / 2 > dokladnosc:
        iteracja += 1
        c = (a + b) / 2
        if funkcja(c) == 0:
            break
        elif funkcja(c) * funkcja(a) < 0:
            b = c
        else:
            a = c

    wynik = (a + b) / 2
    return wynik, iteracja

# Przedział [0, 1] i dokładność e = 0.01
a = 0
b = 1
dokladnosc = 0.01

# Wywołanie funkcji i wyświetlenie wyniku
wynik, iteracja = metoda_bisekcji(funkcja, a, b, dokladnosc)

if wynik is not None:
    print(f"Rozwiązanie równania: x^3 + x - 1 = 0, w przedziale [0, 1] z dokładnością e = 0.01, to x = {wynik}")
    print(f"Liczba iteracji: {iteracja}")
else:
    print("Nie udało się znaleźć rozwiązania.")