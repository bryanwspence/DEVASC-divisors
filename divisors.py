# Create emtpy list that will store Divisors
divisors = []


# Ask user for number, store as integer in number variable
number = int(input("Please enter a number: "))

# Print user's number
print("\nYour number is {}".format(number))

# Calculate Divisors
for x in range(1, number + 1):
    if number % x == 0:
        divisors.append(x)


print("\nThe number {} is divisible by the following numbers {}".format(number, divisors))
