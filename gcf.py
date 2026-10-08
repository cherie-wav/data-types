def gcf():
    number = int(input("give me a number lil bro: "))
    number2 = int(input("give me another number lil bro: "))
    factors = []
    for i in range(1, number):
        if number % i == 0 and number2 % i ==0:
            factors.append(i)
    factors=i+1
    print(factors)
gcf()