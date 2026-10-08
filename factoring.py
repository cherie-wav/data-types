number=int(input("give me a number lil bro: "))
factors = []
for i in range(1, number):
        if number % i == 0:
            factors.append(i)
factors.append(number)
print(factors)