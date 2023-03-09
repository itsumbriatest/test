# Scrivi un programma che scriva i numeri da 1 a 100;
# tuttavia, se il numero è multiplo di 3 deve scrivere
# FIZZ al suo posto, se è multiplo di 5 deve scrivere
# BUZZ e se è multiplo sia di tre che di 5 deve scrivere
# FIZZBUZZ

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
