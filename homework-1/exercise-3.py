num = input("enter any number: ")

if num.isdigit() == True:
    num = float(num)
    print(f"square of your number is: {num*num}")

elif (num[0] == "-"):
    num = num[1:]
    num = float(num)
    print(f"square of your number is: {num*num}")

else:
    num = 0
    print(f"you didn't enter a proper number, so square is: {num*num}")