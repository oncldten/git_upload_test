def fibonacci(stop):
    first = 0
    s = 1
    while s < stop:
        print(s)
        first, s = s, first + s

n = int(input("n = "))
fibonacci(n)
