number = input("enter a number: ")
number_int=int(number)
if number_int > 1:
    if number.isdigit:
        for i in range(2, number_int):
            if number_int % i == 0:
                print(number_int, "is not a prime number")
                break
        else:
            print(number_int, "is a prime number")