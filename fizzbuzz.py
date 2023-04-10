n = 50

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} => FizzBuzz")

    elif i % 2 == 0:
        print(f"{i} => Fizz")

    elif i % 3 == 0:
        print(f"{i} => Buzz")
        
    else:
        print(i)
