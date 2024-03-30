# zad2
import random

# tab = []
# tabLength = int(input("Podaj długość tablicy: "))
#
# for i in range(0, tabLength):
#     print("Podaj tab[", i, "]")
#     tab.append(int(input()))
#
# for i in range(tabLength - 1, -1 , -1):
#     print(tab[i], ", ")

# zad3
#
# tab = []
# tabLength = int(input("Podaj długość tablicy: "))
#
# for i in range(0, tabLength):
#     tab.append(str(random.randrange(-5, 5)))
#
# file = open('result.txt', 'w')
# tab2 = []
# for i in tab: tab2.append(i + '\n')
# file.writelines(tab2)
# file.close()

# zad4

# import numpy as np
# def create_array():
#     array = np.empty((5, 5), dtype=int)
#     array[0] = [2, 3, 4, 5, 6]
#
#     for i in range(1, 5):
#         array[i] = array[i-1] ** 2
#
#     return array
#
# result_array = create_array()
# print("Tablica dwuwymiarowa:")
# print(result_array)

# zad5
#
# def char_histogram(location):
#     histogram = {}
#
#     with open(location, 'r') as file:
#         text = file.read()
#
#     for char in text:
#         if char in histogram:
#             histogram[char] += 1
#         else:
#             histogram[char] = 1
#
#     return histogram
#
# location = 'histogram.txt'
# histogram = char_histogram(location)
# print("Histogram znaków: ")
# for char, count in histogram.items():
#     print(f"'{char}': {count}")

# zad6

# import random
#
# def deck():
#     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     suits = ['c', 'd', 'h', 's']
#     deck = [(rank, suit) for suit in suits for rank in ranks]
#     return deck
#
# def shuffle_deck(deck):
#     shuffled_deck = deck[:]
#     random.shuffle(shuffled_deck)
#     return shuffled_deck
#
# def deal(deck, n):
#     shuffled_deck = shuffle_deck(deck)
#     hands = []
#     for _ in range(n):
#         hand = [shuffled_deck.pop() for _ in range(5)]
#         hands.append(hand)
#     return hands
#
# my_deck = deck()
# print("Nowa talia:")
# print(my_deck)
#
# shuffled_deck = shuffle_deck(my_deck)
# print("\nPotasowana talia:")
# print(shuffled_deck)
#
# hands = deal(my_deck, 4)
# print("\nRozdanie dla 4 graczy:")
# for i, hand in enumerate(hands, 1):
#     print(f"Gracz {i}: {hand}")


