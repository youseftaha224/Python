import random

random_int = random.randint(1,10)
count = 3

while count != 0:
    N = int(input("Please enter a number (1-10): "))
    if N == random_int:
        print("You Guessed Correctly!")
        break
    else:
        count -= 1
        print("Wrong Guess", end=" ")
        print(f"({count} try left)" if count == 1
              else f"({count} tries left)")
else:
    print(f"The number is: {random_int}")

