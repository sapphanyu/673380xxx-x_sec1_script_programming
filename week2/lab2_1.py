num = int(input("Enter a number: ") )
if num < 0:
    text = "The number is negative"
elif num > 0:
    text = "The number is positive"
else:
    text = "The number is zero"

if num == 0:
    print(f"{text}.")
elif num % 2 == 0:
    print(f"{text} and even number.")
else :
    print(f"{text} and odd number.")