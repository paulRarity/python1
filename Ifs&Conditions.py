price = 1000000
good_Credit = True

if good_Credit:
    downPayment = price * 0.1
else:
    downPayment = price * 0.2

message = f'your down payment is: {downPayment}'
print(message)

#####################

price = 1000000
credit = int(input("Your Credit: "))

if credit >= 0.1 * price:
    downPayment = price * 0.1
elif credit >= 0.2 * price:
    downPayment = price * 0.2
else:
    downPayment = price * 0.5

message = f'your down payment is: {downPayment}'
print(message)


#####################
name = input("Your Name: ")

if len(name) < 3 or len(name) > 50:
    print("invalid name")
else:
    print("name looks good")



